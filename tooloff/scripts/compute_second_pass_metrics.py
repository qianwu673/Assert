from __future__ import annotations

from collections import Counter

from common import (
    REPORTS,
    SECOND_PASS_ADJUDICATED,
    SECOND_PASS_COMPLETED,
    SECOND_PASS_KEY,
    md_table,
    read_csv,
)


def cohen_kappa(a: list[str], b: list[str]) -> float:
    if len(a) != len(b):
        raise ValueError("label lists must have equal length")
    n = len(a)
    if n == 0:
        return float("nan")
    observed = sum(x == y for x, y in zip(a, b)) / n
    ca = Counter(a)
    cb = Counter(b)
    labels = set(ca) | set(cb)
    expected = sum((ca[label] / n) * (cb[label] / n) for label in labels)
    return (observed - expected) / (1 - expected)


def main() -> None:
    completed = {r["second_pass_id"]: r for r in read_csv(SECOND_PASS_COMPLETED)}
    key = {r["second_pass_id"]: r for r in read_csv(SECOND_PASS_KEY)}
    ids = sorted(set(completed) & set(key))
    first = [(key[i].get("first_pass_EBC_label") or "").strip() for i in ids]
    second = [(completed[i].get("second_pass_EBC_label") or "").strip() for i in ids]
    matches = sum(a == b for a, b in zip(first, second))
    n = len(ids)
    agreement = 100 * matches / n
    kappa = cohen_kappa(first, second)
    adjudicated = read_csv(SECOND_PASS_ADJUDICATED)

    rows = [
        ["blind second-pass packet size", str(n)],
        ["EBC_label percent agreement", f"{agreement:.1f}%"],
        ["EBC_label Cohen's kappa", f"{kappa:.3f}"],
        ["EBC_label discrepancies adjudicated", str(len(adjudicated))],
    ]

    final_counts = Counter((r.get("final_EBC_label") or "").strip() for r in adjudicated)
    for label in sorted(final_counts):
        rows.append([f"adjudication final {label}", str(final_counts[label])])

    out = "# Reproduced Second-Pass Metrics\n\n" + md_table(["metric", "value"], rows) + "\n"
    REPORTS.mkdir(parents=True, exist_ok=True)
    out_path = REPORTS / "reproduced_second_pass_metrics.md"
    out_path.write_text(out, encoding="utf-8")
    print(out)
    print(f"Wrote {out_path.relative_to(REPORTS.parents[1])}")


if __name__ == "__main__":
    main()
