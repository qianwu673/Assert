from __future__ import annotations

from collections import Counter

from common import (
    EVIDENCE_ORDER,
    FRIENDLY_MODEL_NAMES,
    GEMINI_MODELS,
    PRIMARY_MODELS,
    REPORTS,
    SALIENCE_ORDER,
    count_by,
    group_rows,
    is_unsupported,
    is_violation,
    md_table,
    primary_rows,
    rate,
)


def unsupported_violation_rate(rows):
    unsupported = [r for r in rows if is_unsupported(r)]
    violations = [r for r in unsupported if is_violation(r)]
    return len(violations), len(unsupported)


def main() -> None:
    rows = primary_rows()
    report = ["# Reproduced Main Tables", ""]
    report.append(f"Primary records: {len(rows)}")
    report.append("")

    violations, unsupported_n = unsupported_violation_rate(rows)
    report.append(f"Overall unsupported violation rate: {rate(violations, unsupported_n)}")
    report.append("")

    salience_rows = []
    for salience in SALIENCE_ORDER:
        subset = [r for r in rows if is_unsupported(r) and r.get("salience_condition") == salience]
        v = sum(is_violation(r) for r in subset)
        salience_rows.append([salience, str(len(subset)), str(v), rate(v, len(subset))])
    report.append("## Unsupported Violation Rates By Salience")
    report.append(md_table(["salience", "unsupported n", "violations", "rate"], salience_rows))
    report.append("")

    evidence_rows = []
    for evidence in EVIDENCE_ORDER:
        subset = [r for r in rows if r.get("evidence_condition") == evidence]
        v = sum(is_violation(r) for r in subset)
        evidence_rows.append([evidence, str(len(subset)), str(v), rate(v, len(subset))])
    report.append("## Violation Rates By Evidence Condition")
    report.append(md_table(["evidence", "n", "violations", "rate"], evidence_rows))
    report.append("")

    model_rows = []
    for model in PRIMARY_MODELS:
        subset = [r for r in rows if r.get("model_name") == model]
        unsupported = [r for r in subset if is_unsupported(r)]
        high = [r for r in unsupported if r.get("salience_condition") == "high"]
        uv = sum(is_violation(r) for r in unsupported)
        hv = sum(is_violation(r) for r in high)
        model_rows.append([
            FRIENDLY_MODEL_NAMES[model],
            model,
            str(len(subset)),
            rate(uv, len(unsupported)),
            rate(hv, len(high)),
        ])
    report.append("## Model-Level Unsupported Violation Table")
    report.append(md_table(["model", "alias", "n", "unsupported violation rate", "high-salience unsupported violation rate"], model_rows))
    report.append("")

    gemini_rows = []
    for model in GEMINI_MODELS:
        subset = [r for r in rows if r.get("model_name") == model]
        unsupported = [r for r in subset if is_unsupported(r)]
        total_v = sum(is_violation(r) for r in unsupported)
        row = [FRIENDLY_MODEL_NAMES[model], rate(total_v, len(unsupported))]
        for salience in SALIENCE_ORDER:
            srows = [r for r in unsupported if r.get("salience_condition") == salience]
            row.append(rate(sum(is_violation(r) for r in srows), len(srows)))
        gemini_rows.append(row)
    report.append("## Gemini-Family Table")
    report.append(md_table(["model", "unsupported violations", "low", "medium", "high"], gemini_rows))
    report.append("")

    violation_types = Counter(r.get("violation_type", "") for r in rows if is_violation(r))
    vt_rows = [[k, str(violation_types[k])] for k in sorted(violation_types)]
    report.append("## Violation-Type Distribution")
    report.append(md_table(["violation_type", "count"], vt_rows))
    report.append("")

    residual = [
        r for r in rows
        if is_unsupported(r) and is_violation(r) and r.get("salience_condition") == "high"
    ]
    residual_rows = [[
        FRIENDLY_MODEL_NAMES.get(r.get("model_name"), r.get("model_name", "")),
        r.get("question_id", ""),
        r.get("paper_id", ""),
        r.get("evidence_condition", ""),
        r.get("violation_type", ""),
        r.get("factual_correctness", ""),
    ] for r in residual]
    report.append("## High-Salience Residual Failure Table")
    report.append(md_table(["model", "question_id", "paper_id", "evidence", "violation_type", "factual_correctness"], residual_rows))
    report.append("")

    out = "\n".join(report)
    REPORTS.mkdir(parents=True, exist_ok=True)
    out_path = REPORTS / "reproduced_main_tables.md"
    out_path.write_text(out, encoding="utf-8")
    print(out)
    print(f"\nWrote {out_path.relative_to(REPORTS.parents[1])}")


if __name__ == "__main__":
    main()
