from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORTS = DATA / "reports"
FIGURES = ROOT / "figures"

PRIMARY_CSV = DATA / "annotations" / "stage1_primary810_annotations_adjudicated_v0_3.csv"
ALL_CSV = DATA / "annotations" / "stage1_all1260_annotations_adjudicated_v0_3.csv"
CLAUDE_DEFAULT_CSV = DATA / "annotations" / "stage1_claude_default_sampling_adjudicated_v0_3.csv"
SECOND_PASS_COMPLETED = DATA / "annotations" / "stage1_second_pass_completed.csv"
SECOND_PASS_KEY = DATA / "annotations" / "stage1_second_pass_key_with_first_pass_labels.csv"
SECOND_PASS_ADJUDICATED = DATA / "annotations" / "stage1_second_pass_discrepancies_adjudicated.csv"
MANUSCRIPT_TEX = REPORTS / "evidence_boundary_compliance_technical_report_v0_2.tex"

PRIMARY_MODELS = [
    "anthropic_claude_haiku_4_5",
    "gemini_2_5_flash",
    "gemini_2_5_flash_lite",
    "gemini_2_5_pro",
    "openai_gpt_4_1",
    "openai_gpt_4_1_mini",
    "openai_gpt_4_1_nano",
    "openai_gpt_4o",
    "openai_gpt_4o_mini",
]

FRIENDLY_MODEL_NAMES = {
    "anthropic_claude_haiku_4_5": "Claude Haiku 4.5",
    "gemini_2_5_flash": "Gemini 2.5 Flash",
    "gemini_2_5_flash_lite": "Gemini 2.5 Flash-Lite",
    "gemini_2_5_pro": "Gemini 2.5 Pro",
    "openai_gpt_4_1": "GPT-4.1",
    "openai_gpt_4_1_mini": "GPT-4.1-mini",
    "openai_gpt_4_1_nano": "GPT-4.1-nano",
    "openai_gpt_4o": "GPT-4o",
    "openai_gpt_4o_mini": "GPT-4o-mini",
}

GEMINI_MODELS = [
    "gemini_2_5_flash",
    "gemini_2_5_flash_lite",
    "gemini_2_5_pro",
]

SALIENCE_ORDER = ["low", "medium", "high"]
EVIDENCE_ORDER = ["full", "partial", "none"]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def pct(num: int, den: int) -> str:
    return f"{(100 * num / den):.1f}%" if den else "NA"


def rate(num: int, den: int) -> str:
    return f"{num}/{den} ({pct(num, den)})"


def is_violation(row: dict[str, str]) -> bool:
    return row.get("EBC_label", "").strip() == "violation"


def is_unsupported(row: dict[str, str]) -> bool:
    return row.get("expected_support", "").strip() == "not_supported"


def primary_rows() -> list[dict[str, str]]:
    rows = read_csv(PRIMARY_CSV)
    return [r for r in rows if r.get("model_name") in PRIMARY_MODELS]


def count_by(rows: list[dict[str, str]], key: str) -> Counter:
    return Counter((r.get(key, "") or "").strip() for r in rows)


def group_rows(rows: list[dict[str, str]], key: str) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(row.get(key, "") or "").strip()].append(row)
    return dict(grouped)


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(headers) + " |"]
    out.append("| " + " | ".join("---" for _ in headers) + " |")
    for row in rows:
        out.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(out)
