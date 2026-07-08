from __future__ import annotations

from collections import Counter

from common import (
    EVIDENCE_ORDER,
    MANUSCRIPT_TEX,
    PRIMARY_MODELS,
    SALIENCE_ORDER,
    is_unsupported,
    is_violation,
    primary_rows,
    read_csv,
    SECOND_PASS_ADJUDICATED,
    SECOND_PASS_COMPLETED,
    SECOND_PASS_KEY,
)


EXPECTED_STRINGS = [
    "810 records",
    "405 supported records and 405 unsupported records",
    "94 of 405",
    "23.2\\%",
    "67 of 135",
    "49.6\\%",
    "22 of 135",
    "16.3\\%",
    "5 of 135",
    "3.7\\%",
    "0 violations out of 270",
    "7 violations out of 270",
    "87 violations out of 270",
    "355 records",
    "91.0\\%",
    "0.811",
    "32 \\texttt{EBC\\_label}",
    "31 compliant labels and 1 violation",
    "9 records were adjudicated as \\texttt{disclosed\\_expansion}",
]


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION FAILED: {message}")


def cohen_kappa(a: list[str], b: list[str]) -> float:
    n = len(a)
    observed = sum(x == y for x, y in zip(a, b)) / n
    ca = Counter(a)
    cb = Counter(b)
    labels = set(ca) | set(cb)
    expected = sum((ca[label] / n) * (cb[label] / n) for label in labels)
    return (observed - expected) / (1 - expected)


def main() -> None:
    rows = primary_rows()
    if len(rows) != 810:
        fail(f"primary record count is {len(rows)}, expected 810")
    if sorted(set(r["model_name"] for r in rows)) != sorted(PRIMARY_MODELS):
        fail("primary model set does not match expected model set")

    support_counts = Counter(r["expected_support"] for r in rows)
    if support_counts["supported"] != 405 or support_counts["not_supported"] != 405:
        fail(f"support counts are {dict(support_counts)}, expected 405/405")

    unsupported = [r for r in rows if is_unsupported(r)]
    unsupported_violations = sum(is_violation(r) for r in unsupported)
    if unsupported_violations != 94:
        fail(f"unsupported violations are {unsupported_violations}, expected 94")

    expected_salience = {"low": (67, 135), "medium": (22, 135), "high": (5, 135)}
    for salience in SALIENCE_ORDER:
        subset = [r for r in unsupported if r["salience_condition"] == salience]
        got = (sum(is_violation(r) for r in subset), len(subset))
        if got != expected_salience[salience]:
            fail(f"{salience} salience got {got}, expected {expected_salience[salience]}")

    expected_evidence = {"full": (0, 270), "partial": (7, 270), "none": (87, 270)}
    for evidence in EVIDENCE_ORDER:
        subset = [r for r in rows if r["evidence_condition"] == evidence]
        got = (sum(is_violation(r) for r in subset), len(subset))
        if got != expected_evidence[evidence]:
            fail(f"{evidence} evidence got {got}, expected {expected_evidence[evidence]}")

    high_residual = [
        r for r in unsupported
        if r["salience_condition"] == "high" and is_violation(r)
    ]
    if len(high_residual) != 5:
        fail(f"high-salience residual failures are {len(high_residual)}, expected 5")
    by_model = Counter(r["model_name"] for r in high_residual)
    expected_models = {
        "gemini_2_5_flash_lite": 3,
        "gemini_2_5_pro": 1,
        "openai_gpt_4o": 1,
    }
    if dict(by_model) != expected_models:
        fail(f"high-salience residual models are {dict(by_model)}, expected {expected_models}")

    completed = {r["second_pass_id"]: r for r in read_csv(SECOND_PASS_COMPLETED)}
    key = {r["second_pass_id"]: r for r in read_csv(SECOND_PASS_KEY)}
    ids = sorted(set(completed) & set(key))
    first = [(key[i].get("first_pass_EBC_label") or "").strip() for i in ids]
    second = [(completed[i].get("second_pass_EBC_label") or "").strip() for i in ids]
    matches = sum(a == b for a, b in zip(first, second))
    agreement = round(100 * matches / len(ids), 1)
    kappa = round(cohen_kappa(first, second), 3)
    if len(ids) != 355 or agreement != 91.0 or kappa != 0.811:
        fail(f"second-pass metrics got n={len(ids)}, agreement={agreement}, kappa={kappa}")

    adjudicated = read_csv(SECOND_PASS_ADJUDICATED)
    final = Counter((r.get("final_EBC_label") or "").strip() for r in adjudicated)
    if len(adjudicated) != 32 or final["compliant"] != 31 or final["violation"] != 1:
        fail(f"adjudication got n={len(adjudicated)}, final={dict(final)}")

    manuscript = MANUSCRIPT_TEX.read_text(encoding="utf-8")
    missing = [s for s in EXPECTED_STRINGS if s not in manuscript]
    if missing:
        fail("manuscript missing expected strings: " + "; ".join(missing))

    print("All reported manuscript counts reproduced exactly.")


if __name__ == "__main__":
    main()
