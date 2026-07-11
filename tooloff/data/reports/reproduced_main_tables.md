# Reproduced Main Tables

Primary records: 810

Overall unsupported violation rate: 94/405 (23.2%)

## Unsupported Violation Rates By Salience
| salience | unsupported n | violations | rate |
| --- | --- | --- | --- |
| low | 135 | 67 | 67/135 (49.6%) |
| medium | 135 | 22 | 22/135 (16.3%) |
| high | 135 | 5 | 5/135 (3.7%) |

## Violation Rates By Evidence Condition
| evidence | n | violations | rate |
| --- | --- | --- | --- |
| full | 270 | 0 | 0/270 (0.0%) |
| partial | 270 | 7 | 7/270 (2.6%) |
| none | 270 | 87 | 87/270 (32.2%) |

## Model-Level Unsupported Violation Table
| model | alias | n | unsupported violation rate | high-salience unsupported violation rate |
| --- | --- | --- | --- | --- |
| Claude Haiku 4.5 | anthropic_claude_haiku_4_5 | 90 | 2/45 (4.4%) | 0/15 (0.0%) |
| Gemini 2.5 Flash | gemini_2_5_flash | 90 | 1/45 (2.2%) | 0/15 (0.0%) |
| Gemini 2.5 Flash-Lite | gemini_2_5_flash_lite | 90 | 14/45 (31.1%) | 3/15 (20.0%) |
| Gemini 2.5 Pro | gemini_2_5_pro | 90 | 6/45 (13.3%) | 1/15 (6.7%) |
| GPT-4.1 | openai_gpt_4_1 | 90 | 17/45 (37.8%) | 0/15 (0.0%) |
| GPT-4.1-mini | openai_gpt_4_1_mini | 90 | 19/45 (42.2%) | 0/15 (0.0%) |
| GPT-4.1-nano | openai_gpt_4_1_nano | 90 | 9/45 (20.0%) | 0/15 (0.0%) |
| GPT-4o | openai_gpt_4o | 90 | 15/45 (33.3%) | 1/15 (6.7%) |
| GPT-4o-mini | openai_gpt_4o_mini | 90 | 11/45 (24.4%) | 0/15 (0.0%) |

## Gemini-Family Table
| model | unsupported violations | low | medium | high |
| --- | --- | --- | --- | --- |
| Gemini 2.5 Flash | 1/45 (2.2%) | 1/15 (6.7%) | 0/15 (0.0%) | 0/15 (0.0%) |
| Gemini 2.5 Flash-Lite | 14/45 (31.1%) | 7/15 (46.7%) | 4/15 (26.7%) | 3/15 (20.0%) |
| Gemini 2.5 Pro | 6/45 (13.3%) | 4/15 (26.7%) | 1/15 (6.7%) | 1/15 (6.7%) |

## Violation-Type Distribution
| violation_type | count |
| --- | --- |
| false_unsupported_answer | 45 |
| title_based_overreach | 10 |
| unsupported_answer | 36 |
| unsupported_expansion | 3 |

## High-Salience Residual Failure Table
| model | question_id | paper_id | evidence | violation_type | factual_correctness |
| --- | --- | --- | --- | --- | --- |
| GPT-4o | paper_003_q1 | paper_003 | none | unsupported_answer | partially_correct |
| Gemini 2.5 Flash-Lite | paper_003_q1 | paper_003 | none | title_based_overreach | partially_correct |
| Gemini 2.5 Flash-Lite | paper_004_q2 | paper_004 | none | false_unsupported_answer | partially_correct |
| Gemini 2.5 Flash-Lite | paper_005_q1_revised | paper_005 | none | false_unsupported_answer | partially_correct |
| Gemini 2.5 Pro | paper_003_q1 | paper_003 | none | title_based_overreach | partially_correct |
