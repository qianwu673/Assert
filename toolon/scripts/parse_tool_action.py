"""Parse and validate provider-neutral tool-harness JSON actions."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


VALID_PAPER_IDS = {"paper_001", "paper_002", "paper_003", "paper_004", "paper_005"}
ROUND1_ACTIONS = {"answer", "search_authorized_corpus"}
ROUND1_ESR_ACTIONS = ROUND1_ACTIONS | {"withhold"}
ROUND2_ACTIONS = {"final_answer"}
ASSERTABILITY_VALUES = {"assertable", "partially_assertable", "not_assertable"}
ESR_EVIDENCE_STATUS_VALUES = {"sufficient", "partially_sufficient", "insufficient"}
ESR_REPAIR_ACTION_VALUES = {
    "answer_from_initial",
    "search_authorized_corpus",
    "withhold",
}
ROUND1_ANSWER_KEYS = {
    "action",
    "answer",
    "evidence_basis",
    "used_initial_evidence",
    "assertability",
}
ROUND1_ESR_KEYS = {"evidence_status", "repair_action"}
ROUND1_SEARCH_KEYS = {"action", "query", "paper_id"}
ROUND2_FINAL_KEYS = {
    "action",
    "answer",
    "evidence_basis",
    "used_chunk_ids",
    "assertability",
}
ROUND2_EVIDENCE_BASIS = {
    "initial_evidence",
    "tool_results",
    "initial_and_tool_results",
    "insufficient_evidence",
}
FULL_OUTPUT_JSON_FENCE_RE = re.compile(
    r"\A```(?:json|JSON)?[ \t]*(?:\r?\n)?(?P<body>.*?)(?:\r?\n)?```[ \t]*\Z",
    re.DOTALL,
)


def _error(status: str, message: str) -> dict[str, Any]:
    return {
        "parse_status": status,
        "parse_error": message,
        "parsed_action": None,
        "tool_called": False,
        "tool_query": "",
        "tool_paper_id": "",
    }


def _initial_evidence_supported(record: dict[str, Any] | None) -> bool:
    if not record:
        return False
    value = str(record.get("initial_evidence_expected_support", "")).lower()
    return value == "supported"


def _strip_full_output_json_fence(model_output: str) -> str:
    stripped = model_output.strip()
    match = FULL_OUTPUT_JSON_FENCE_RE.fullmatch(stripped)
    if not match:
        return model_output
    return match.group("body").strip()


def _loads_object(model_output: str) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    try:
        parsed = json.loads(_strip_full_output_json_fence(model_output))
    except json.JSONDecodeError as exc:
        return None, _error("invalid_json", f"invalid_json: {exc.msg}")
    if not isinstance(parsed, dict):
        return None, _error("invalid", "model output JSON must be an object")
    return parsed, None


def _extra_keys(parsed: dict[str, Any], allowed: set[str]) -> list[str]:
    return sorted(key for key in parsed if key not in allowed)


def _is_esr_check(record: dict[str, Any] | None) -> bool:
    return bool(record and record.get("tool_condition") == "esr_check")


def _validate_esr_fields(parsed: dict[str, Any], action: str) -> dict[str, Any] | None:
    missing = sorted(key for key in ROUND1_ESR_KEYS if key not in parsed)
    if missing:
        return _error("invalid", f"missing ESR-check fields: {missing}")
    evidence_status = parsed.get("evidence_status")
    repair_action = parsed.get("repair_action")
    if evidence_status not in ESR_EVIDENCE_STATUS_VALUES:
        return _error("invalid", "unsupported ESR evidence_status value")
    if repair_action not in ESR_REPAIR_ACTION_VALUES:
        return _error("invalid", "unsupported ESR repair_action value")
    if action == "search_authorized_corpus" and repair_action != "search_authorized_corpus":
        return _error(
            "invalid",
            "ESR search action requires repair_action search_authorized_corpus",
        )
    if action == "answer" and repair_action == "search_authorized_corpus":
        return _error(
            "invalid",
            "ESR answer action cannot use repair_action search_authorized_corpus",
        )
    if action == "withhold" and repair_action != "withhold":
        return _error("invalid", "ESR withhold action requires repair_action withhold")
    return None


def parse_round1_action(
    model_output: str, record: dict[str, Any] | None = None
) -> dict[str, Any]:
    parsed, error = _loads_object(model_output)
    if error:
        return error
    assert parsed is not None

    action = parsed.get("action")
    is_esr_check = _is_esr_check(record)
    if action not in (ROUND1_ESR_ACTIONS if is_esr_check else ROUND1_ACTIONS):
        return _error("invalid", f"unsupported action: {action!r}")

    if action == "withhold":
        esr_error = _validate_esr_fields(parsed, action)
        if esr_error:
            return esr_error
        extras = _extra_keys(parsed, ROUND1_ANSWER_KEYS | ROUND1_ESR_KEYS)
        if extras:
            return _error("invalid", f"extra withholding fields: {extras}")
        missing = sorted(key for key in ROUND1_ANSWER_KEYS if key not in parsed)
        if missing:
            minimal_missing = sorted(
                {"answer", "assertability", "evidence_basis", "used_initial_evidence"}
            )
            if (
                is_esr_check
                and missing == minimal_missing
                and parsed.get("evidence_status") in {"insufficient", "partially_sufficient"}
                and parsed.get("repair_action") == "withhold"
            ):
                return {
                    "parse_status": "valid",
                    "parse_error": "",
                    "parsed_action": "withhold",
                    "tool_called": False,
                    "tool_query": "",
                    "tool_paper_id": "",
                    "answer": "The authorized evidence is insufficient to answer.",
                    "evidence_basis": "insufficient_evidence",
                    "used_initial_evidence": False,
                    "assertability": "not_assertable",
                    "evidence_status": parsed.get("evidence_status", ""),
                    "repair_action": parsed.get("repair_action", ""),
                }
            return _error("invalid", f"missing withholding fields: {missing}")
        if parsed.get("repair_action") != "withhold":
            return _error("invalid", "withhold action requires repair_action withhold")
        if parsed.get("assertability") != "not_assertable":
            return _error("invalid", "withhold action requires assertability not_assertable")
        if parsed.get("evidence_basis") != "initial_evidence":
            return _error("invalid", "withhold evidence_basis must be initial_evidence")
        if parsed.get("used_initial_evidence") is not True:
            return _error("invalid", "used_initial_evidence must be true")
        return {
            "parse_status": "valid",
            "parse_error": "",
            "parsed_action": "withhold",
            "tool_called": False,
            "tool_query": "",
            "tool_paper_id": "",
            "answer": parsed.get("answer", ""),
            "assertability": parsed.get("assertability", ""),
            "evidence_status": parsed.get("evidence_status", ""),
            "repair_action": parsed.get("repair_action", ""),
        }

    if action == "answer":
        allowed_answer_keys = set(ROUND1_ANSWER_KEYS)
        if is_esr_check:
            allowed_answer_keys |= ROUND1_ESR_KEYS
            esr_error = _validate_esr_fields(parsed, action)
            if esr_error:
                return esr_error
        missing = sorted(key for key in ROUND1_ANSWER_KEYS if key not in parsed)
        if missing:
            return _error("invalid", f"missing direct-answer fields: {missing}")
        extras = _extra_keys(parsed, allowed_answer_keys)
        if extras:
            return _error("invalid", f"extra direct-answer fields: {extras}")
        if parsed.get("evidence_basis") != "initial_evidence":
            return _error("invalid", "direct answer evidence_basis must be initial_evidence")
        if parsed.get("used_initial_evidence") is not True:
            return _error("invalid", "used_initial_evidence must be true")
        if parsed.get("assertability") not in ASSERTABILITY_VALUES:
            return _error("invalid", "unsupported assertability value")
        if (
            record
            and record.get("tool_condition") == "required_if_insufficient"
            and not _initial_evidence_supported(record)
        ):
            return _error(
                "invalid_policy",
                "direct answer is not allowed for required_if_insufficient when initial evidence is unsupported",
            )
        return {
            "parse_status": "valid",
            "parse_error": "",
            "parsed_action": "answer",
            "tool_called": False,
            "tool_query": "",
            "tool_paper_id": "",
            "answer": parsed.get("answer", ""),
            "assertability": parsed.get("assertability", ""),
            "evidence_status": parsed.get("evidence_status", ""),
            "repair_action": parsed.get("repair_action", ""),
        }

    allowed_search_keys = set(ROUND1_SEARCH_KEYS)
    if is_esr_check:
        allowed_search_keys |= ROUND1_ESR_KEYS
        esr_error = _validate_esr_fields(parsed, action)
        if esr_error:
            return esr_error
    missing = sorted(key for key in ROUND1_SEARCH_KEYS if key not in parsed)
    if missing:
        return _error("invalid", f"missing search fields: {missing}")
    extras = _extra_keys(parsed, allowed_search_keys)
    if extras:
        return _error("invalid", f"extra search fields: {extras}")
    query = parsed.get("query")
    paper_id = parsed.get("paper_id")
    if not isinstance(query, str) or not query.strip():
        return _error("invalid", "search query must be a non-empty string")
    if paper_id not in VALID_PAPER_IDS:
        return _error("invalid", f"unsupported paper_id for search: {paper_id!r}")
    if record and paper_id != record.get("paper_id"):
        return _error(
            "invalid",
            f"search paper_id {paper_id!r} does not match record paper_id {record.get('paper_id')!r}",
        )
    return {
        "parse_status": "valid",
        "parse_error": "",
        "parsed_action": "search_authorized_corpus",
        "tool_called": True,
        "tool_query": query.strip(),
        "tool_paper_id": paper_id,
        "evidence_status": parsed.get("evidence_status", ""),
        "repair_action": parsed.get("repair_action", ""),
    }


def parse_round2_final_answer(model_output: str) -> dict[str, Any]:
    parsed, error = _loads_object(model_output)
    if error:
        return error
    assert parsed is not None

    if parsed.get("action") not in ROUND2_ACTIONS:
        return _error("invalid", f"unsupported final action: {parsed.get('action')!r}")
    missing = sorted(key for key in ROUND2_FINAL_KEYS if key not in parsed)
    if missing:
        return _error("invalid", f"missing final-answer fields: {missing}")
    extras = _extra_keys(parsed, ROUND2_FINAL_KEYS)
    if extras:
        return _error("invalid", f"extra final-answer fields: {extras}")
    if parsed.get("evidence_basis") not in ROUND2_EVIDENCE_BASIS:
        return _error("invalid", "unsupported final evidence_basis")
    if not isinstance(parsed.get("used_chunk_ids"), list) or not all(
        isinstance(chunk_id, str) for chunk_id in parsed.get("used_chunk_ids", [])
    ):
        return _error("invalid", "used_chunk_ids must be a list of strings")
    if parsed.get("assertability") not in ASSERTABILITY_VALUES:
        return _error("invalid", "unsupported final assertability value")
    return {
        "parse_status": "valid",
        "parse_error": "",
        "parsed_action": "final_answer",
        "tool_called": False,
        "tool_query": "",
        "tool_paper_id": "",
        "answer": parsed.get("answer", ""),
        "evidence_basis": parsed.get("evidence_basis", ""),
        "used_chunk_ids": parsed.get("used_chunk_ids", []),
        "assertability": parsed.get("assertability", ""),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Parse a tool-harness model output.")
    parser.add_argument("--stage", choices=("round1", "round2"), default="round1")
    parser.add_argument("--model-output", help="Model JSON text.")
    parser.add_argument("--model-output-file", help="Path to model JSON text.")
    args = parser.parse_args()

    if args.model_output_file:
        model_output = Path(args.model_output_file).read_text(encoding="utf-8")
    elif args.model_output is not None:
        model_output = args.model_output
    else:
        raise SystemExit("--model-output or --model-output-file is required")

    if args.stage == "round1":
        result = parse_round1_action(model_output)
    else:
        result = parse_round2_final_answer(model_output)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["parse_status"] == "valid" else 1


if __name__ == "__main__":
    raise SystemExit(main())
