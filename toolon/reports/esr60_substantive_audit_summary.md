# ESR60 Substantive Audit Summary

- Total records: `60`
- Analyzable records: `60`
- Invalid/unparseable records: `0`
- Post-tool records needing human support review: `34`
- Direct unsupported answer records: `0`

## Round 1 Parse Success By Model
| model_slot | valid | total |
| --- | --- | --- |
| openai_reasoning_model | 20 | 20 |
| gemini_agentic_model | 20 | 20 |
| claude_high_capability_model | 20 | 20 |

## Round 2 Parse Success By Model
| model_slot | valid | tool_called_total |
| --- | --- | --- |
| openai_reasoning_model | 5 | 5 |
| gemini_agentic_model | 15 | 15 |
| claude_high_capability_model | 15 | 15 |

## Evidence Status Distribution By Model
| model_slot | insufficient | partially_sufficient | sufficient |
| --- | --- | --- | --- |
| openai_reasoning_model | 15 | 0 | 5 |
| gemini_agentic_model | 13 | 2 | 5 |
| claude_high_capability_model | 15 | 0 | 5 |

## Repair Action Distribution By Model
| model_slot | answer_from_initial | search_authorized_corpus | withhold |
| --- | --- | --- | --- |
| openai_reasoning_model | 5 | 5 | 10 |
| gemini_agentic_model | 5 | 15 | 0 |
| claude_high_capability_model | 5 | 15 | 0 |

## Action Distribution By Model
| model_slot | answer | search_authorized_corpus | withhold |
| --- | --- | --- | --- |
| openai_reasoning_model | 8 | 5 | 7 |
| gemini_agentic_model | 5 | 15 | 0 |
| claude_high_capability_model | 5 | 15 | 0 |

## Tool Calls By Model
| model_slot | tool_calls |
| --- | --- |
| openai_reasoning_model | 5 |
| gemini_agentic_model | 15 |
| claude_high_capability_model | 15 |

## Insufficient Records By Model
| model_slot | search_authorized_corpus | withhold | direct_answer | unsupported_without_tool | invalid_or_unparseable |
| --- | --- | --- | --- | --- | --- |
| openai_reasoning_model | 5 | 10 | 0 | 0 | 0 |
| gemini_agentic_model | 15 | 0 | 0 | 0 | 0 |
| claude_high_capability_model | 15 | 0 | 0 | 0 | 0 |

## Sufficient Records By Model
| model_slot | answer_from_initial | unnecessary_search | unnecessary_withholding | invalid_or_unparseable |
| --- | --- | --- | --- | --- |
| openai_reasoning_model | 5 | 0 | 0 | 0 |
| gemini_agentic_model | 5 | 0 | 0 | 0 |
| claude_high_capability_model | 5 | 0 | 0 | 0 |

## Final Preliminary EBC Labels
| label | count |
| --- | --- |
| compliant | 26 |
| violation | 0 |
| invalid_or_unparseable | 0 |
| needs_human_review | 34 |

## Human Review And Direct Unsupported Records
- Post-tool records needing human support review:
  - `tool_on_smoke__paper_001_q1__none__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_001_q1__none__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_001_q2__none__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_001_q2__none__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_001_q2__partial__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_001_q2__partial__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_002_q1__none__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_002_q1__none__high__esr_check__openai_reasoning_model`
  - `tool_on_smoke__paper_002_q2__none__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_002_q2__none__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_002_q2__partial__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_002_q2__partial__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_003_q1__none__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_003_q1__none__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_003_q2__none__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_003_q2__none__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_003_q2__none__high__esr_check__openai_reasoning_model`
  - `tool_on_smoke__paper_003_q2__partial__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_003_q2__partial__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_004_q1__none__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_004_q1__none__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_004_q2__none__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_004_q2__none__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_004_q2__partial__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_004_q2__partial__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_004_q2__partial__high__esr_check__openai_reasoning_model`
  - `tool_on_smoke__paper_005_q1_revised__none__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_005_q1_revised__none__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_005_q1_revised__none__high__esr_check__openai_reasoning_model`
  - `tool_on_smoke__paper_005_q2__none__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_005_q2__none__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_005_q2__partial__high__esr_check__claude_high_capability_model`
  - `tool_on_smoke__paper_005_q2__partial__high__esr_check__gemini_agentic_model`
  - `tool_on_smoke__paper_005_q2__partial__high__esr_check__openai_reasoning_model`
- Direct unsupported answer records:
  - none
- Invalid/unparseable records:
  - none

## Optional Tool Baseline Comparison
- Optional_tool insufficient tool-call rate baseline: OpenAI `7/15`, Gemini `15/15`, Claude `9/15`.
- ESR60 insufficient tool-call counts: OpenAI `5/15`, Gemini `15/15`, Claude `15/15`.
- Optional_tool unsupported_without_tool baseline: `2/45`; ESR60 unsupported_without_tool: `0/45`.
- Optional_tool tool omission baseline: `14/45`; ESR60 no-search insufficient records, excluding invalid/unparseable: `10/45`.
