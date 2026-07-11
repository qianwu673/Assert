"""Build provider-neutral Round 1 prompt previews for all tool-on records.

The generated JSONL intentionally contains prompt previews. By default, long
initial evidence text is replaced with a placeholder so public artifacts do not
redistribute paper excerpts. Use --include-full-evidence only for a local API
runner that must send the complete prompt to a model.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


TOOL_ON_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = TOOL_ON_ROOT.parent
RECORDS_PATH = TOOL_ON_ROOT / "data" / "items_tool_on.jsonl"
ROUND1_TEMPLATE_PATH = TOOL_ON_ROOT / "prompts" / "round1_tool_protocol.txt"
ROUND1_ESR_CHECK_TEMPLATE_PATH = (
    TOOL_ON_ROOT / "prompts" / "round1_esr_check_tool_protocol.txt"
)
OUTPUT_PATH = TOOL_ON_ROOT / "data" / "derived" / "round1_prompt_previews.jsonl"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path} line {line_number}: {exc}")
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def prompt_safe_initial_evidence(record: dict[str, Any], include_full: bool) -> str:
    if include_full:
        return str(record.get("initial_evidence_packet", "")).strip()
    evidence_condition = record.get("evidence_condition", "")
    evidence_path = record.get("initial_evidence_path", "")
    return (
        "[Initial evidence packet omitted from this preview. "
        f"Runtime harness inserts the record's {evidence_condition!r} initial "
        f"evidence packet from {evidence_path!r} here.]"
    )


def render_round1_prompt(record: dict[str, Any], include_full_evidence: bool = False) -> str:
    template_path = (
        ROUND1_ESR_CHECK_TEMPLATE_PATH
        if record.get("tool_condition") == "esr_check"
        else ROUND1_TEMPLATE_PATH
    )
    template = template_path.read_text(encoding="utf-8")
    values = {
        "record_id": record.get("record_id", ""),
        "model_slot": record.get("model_slot", ""),
        "paper_id": record.get("paper_id", ""),
        "question_id": record.get("question_id", ""),
        "question_type": record.get("question_type", ""),
        "evidence_condition": record.get("evidence_condition", ""),
        "tool_condition": record.get("tool_condition", ""),
        "initial_evidence_expected_support": record.get(
            "initial_evidence_expected_support", ""
        ),
        "initial_evidence_packet": prompt_safe_initial_evidence(
            record, include_full=include_full_evidence
        ),
        "target_question": record.get("target_question", ""),
    }
    return template.format(**values).strip()


def build_prompt_rows(
    records: list[dict[str, Any]], include_full_evidence: bool = False
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for record in records:
        rows.append(
            {
                "record_id": record.get("record_id", ""),
                "model_slot": record.get("model_slot", ""),
                "paper_id": record.get("paper_id", ""),
                "question_id": record.get("question_id", ""),
                "question_type": record.get("question_type", ""),
                "evidence_condition": record.get("evidence_condition", ""),
                "tool_condition": record.get("tool_condition", ""),
                "initial_evidence_expected_support": record.get(
                    "initial_evidence_expected_support", ""
                ),
                "target_question": record.get("target_question", ""),
                "round1_prompt": render_round1_prompt(
                    record, include_full_evidence=include_full_evidence
                ),
                "prompt_text_mode": (
                    "full_initial_evidence"
                    if include_full_evidence
                    else "preview_initial_evidence_placeholder"
                ),
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Round 1 prompt previews.")
    parser.add_argument(
        "--records",
        default=str(RECORDS_PATH),
        help="Tool-on record JSONL path.",
    )
    parser.add_argument(
        "--output",
        default=str(OUTPUT_PATH),
        help="Output JSONL path.",
    )
    parser.add_argument(
        "--include-full-evidence",
        action="store_true",
        help="Insert full initial evidence text. Intended only for local API runners.",
    )
    args = parser.parse_args()

    records = read_jsonl(Path(args.records))
    rows = build_prompt_rows(
        records, include_full_evidence=bool(args.include_full_evidence)
    )
    write_jsonl(Path(args.output), rows)
    print(
        json.dumps(
            {
                "round1_prompts_written": len(rows),
                "output": str(Path(args.output).as_posix()),
                "prompt_text_mode": rows[0]["prompt_text_mode"] if rows else "",
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
