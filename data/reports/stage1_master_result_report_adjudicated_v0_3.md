# Stage 1 Master Result Report, Adjudicated v0.3

## Executive Summary

After blind second-pass review and adjudication, the Stage 1 results continue to support the central finding that evidence-boundary compliance is condition-sensitive and model-sensitive. Across the adjudicated primary temperature-controlled comparison, unsupported-condition violations occurred in 94/405 (23.2%) unsupported records. This pattern indicates that the evaluated behavior is not merely a matter of factual correctness, but whether a model treats the provided material as the authorized evidentiary boundary.

Boundary salience substantially reduced unsupported-condition violations after adjudication. In the primary comparison, unsupported-condition violation rates were 67/135 (49.6%) under low salience, 22/135 (16.3%) under medium salience, and 5/135 (3.7%) under high salience. High salience therefore improved compliance for most but not all models and cases.

Provider and model-family differences remained visible after adjudication. OpenAI, Claude, and Gemini models differed in unsupported violation rates, high-salience residual failures, and tendencies to refuse, answer, partially answer, or disclose expansion. The results are therefore best interpreted as evidence of model-level boundary sensitivity rather than a uniform provider-independent effect.

Residual high-salience failures persisted after adjudication: 5 high-salience unsupported records in the primary comparison were labeled as violations. The adjudication also added one high-salience Gemini 2.5 Pro violation relative to the pre-adjudication primary file (0 before, 1 after).

The Claude-family default-sampling extension retained a disclosed-expansion finding after adjudication, but the count decreased because several Fable 5 first-pass disclosed-expansion labels were adjudicated as compliant refusals or title-scoped partial answers rather than actual external expansions. The adjudicated Claude default-sampling file contains 9 disclosed-expansion records, including 9 for Claude Fable 5.

## Dataset and Design Summary

The adjudicated primary comparison contains 810 records. It covers 5 papers and 10 question IDs, crossed with evidence conditions `full, partial, none` and salience conditions `low, medium, high`. Each model contributes 90 records.

### Records Per Model, Primary Comparison

| model | records |
| --- | --- |
| anthropic_claude_haiku_4_5 | 90 |
| gemini_2_5_flash | 90 |
| gemini_2_5_flash_lite | 90 |
| gemini_2_5_pro | 90 |
| openai_gpt_4_1 | 90 |
| openai_gpt_4_1_mini | 90 |
| openai_gpt_4_1_nano | 90 |
| openai_gpt_4o | 90 |
| openai_gpt_4o_mini | 90 |

### Supported vs Unsupported Records, Primary Comparison

| expected_support | records |
| --- | --- |
| not_supported | 405 |
| supported | 405 |

Supported records are cases where the provided material is expected to contain enough evidence to answer. Unsupported records are cases where the answer is not licensed by the provided material, either because the evidence condition is `none` or because a target-section-required question is paired with insufficient evidence.

## Primary Temperature-Controlled Comparison

Input file: `results/annotation_adjudicated/stage1_all810_annotations_main540_plus_gemini_2_5_family_adjudicated_v0_3.csv`

Total records: 810

Models: `anthropic_claude_haiku_4_5`, `gemini_2_5_flash`, `gemini_2_5_flash_lite`, `gemini_2_5_pro`, `openai_gpt_4_1`, `openai_gpt_4_1_mini`, `openai_gpt_4_1_nano`, `openai_gpt_4o`, `openai_gpt_4o_mini`

### EBC Label Counts By Model

| model | n | compliant | violation | disclosed_expansion | unclear |
| --- | --- | --- | --- | --- | --- |
| anthropic_claude_haiku_4_5 | 90 | 88 | 2 | 0 | 0 |
| gemini_2_5_flash | 90 | 89 | 1 | 0 | 0 |
| gemini_2_5_flash_lite | 90 | 76 | 14 | 0 | 0 |
| gemini_2_5_pro | 90 | 84 | 6 | 0 | 0 |
| openai_gpt_4_1 | 90 | 73 | 17 | 0 | 0 |
| openai_gpt_4_1_mini | 90 | 71 | 19 | 0 | 0 |
| openai_gpt_4_1_nano | 90 | 81 | 9 | 0 | 0 |
| openai_gpt_4o | 90 | 75 | 15 | 0 | 0 |
| openai_gpt_4o_mini | 90 | 79 | 11 | 0 | 0 |

### Model-Level Unsupported Violation Summary

| model | n | unsupported violation rate | high-salience unsupported violation rate | disclosed_expansion count |
| --- | --- | --- | --- | --- |
| anthropic_claude_haiku_4_5 | 90 | 2/45 (4.4%) | 0/15 (0.0%) | 0 |
| gemini_2_5_flash | 90 | 1/45 (2.2%) | 0/15 (0.0%) | 0 |
| gemini_2_5_flash_lite | 90 | 14/45 (31.1%) | 3/15 (20.0%) | 0 |
| gemini_2_5_pro | 90 | 6/45 (13.3%) | 1/15 (6.7%) | 0 |
| openai_gpt_4_1 | 90 | 17/45 (37.8%) | 0/15 (0.0%) | 0 |
| openai_gpt_4_1_mini | 90 | 19/45 (42.2%) | 0/15 (0.0%) | 0 |
| openai_gpt_4_1_nano | 90 | 9/45 (20.0%) | 0/15 (0.0%) | 0 |
| openai_gpt_4o | 90 | 15/45 (33.3%) | 1/15 (6.7%) | 0 |
| openai_gpt_4o_mini | 90 | 11/45 (24.4%) | 0/15 (0.0%) | 0 |

### Provider / Model-Family Summary

| provider/model family | models | records | unsupported violation rate | high-salience unsupported violation rate |
| --- | --- | --- | --- | --- |
| Anthropic/Claude | 1 | 90 | 2/45 (4.4%) | 0/15 (0.0%) |
| Google Gemini | 3 | 270 | 21/135 (15.6%) | 4/45 (8.9%) |
| OpenAI | 5 | 450 | 71/225 (31.6%) | 1/75 (1.3%) |

### Unsupported-Condition Violation Rates By Salience

| salience | unsupported n | violations | violation rate |
| --- | --- | --- | --- |
| low | 135 | 67 | 49.6% |
| medium | 135 | 22 | 16.3% |
| high | 135 | 5 | 3.7% |

### Unsupported-Condition Violation Rates By Model And Salience

| model | salience | unsupported n | violations | violation rate |
| --- | --- | --- | --- | --- |
| anthropic_claude_haiku_4_5 | low | 15 | 2 | 13.3% |
| anthropic_claude_haiku_4_5 | medium | 15 | 0 | 0.0% |
| anthropic_claude_haiku_4_5 | high | 15 | 0 | 0.0% |
| gemini_2_5_flash | low | 15 | 1 | 6.7% |
| gemini_2_5_flash | medium | 15 | 0 | 0.0% |
| gemini_2_5_flash | high | 15 | 0 | 0.0% |
| gemini_2_5_flash_lite | low | 15 | 7 | 46.7% |
| gemini_2_5_flash_lite | medium | 15 | 4 | 26.7% |
| gemini_2_5_flash_lite | high | 15 | 3 | 20.0% |
| gemini_2_5_pro | low | 15 | 4 | 26.7% |
| gemini_2_5_pro | medium | 15 | 1 | 6.7% |
| gemini_2_5_pro | high | 15 | 1 | 6.7% |
| openai_gpt_4_1 | low | 15 | 13 | 86.7% |
| openai_gpt_4_1 | medium | 15 | 4 | 26.7% |
| openai_gpt_4_1 | high | 15 | 0 | 0.0% |
| openai_gpt_4_1_mini | low | 15 | 12 | 80.0% |
| openai_gpt_4_1_mini | medium | 15 | 7 | 46.7% |
| openai_gpt_4_1_mini | high | 15 | 0 | 0.0% |
| openai_gpt_4_1_nano | low | 15 | 8 | 53.3% |
| openai_gpt_4_1_nano | medium | 15 | 1 | 6.7% |
| openai_gpt_4_1_nano | high | 15 | 0 | 0.0% |
| openai_gpt_4o | low | 15 | 10 | 66.7% |
| openai_gpt_4o | medium | 15 | 4 | 26.7% |
| openai_gpt_4o | high | 15 | 1 | 6.7% |
| openai_gpt_4o_mini | low | 15 | 10 | 66.7% |
| openai_gpt_4o_mini | medium | 15 | 1 | 6.7% |
| openai_gpt_4o_mini | high | 15 | 0 | 0.0% |

### Violation Rates By Evidence Condition

| evidence condition | n | violations | violation rate |
| --- | --- | --- | --- |
| full | 270 | 0 | 0.0% |
| partial | 270 | 7 | 2.6% |
| none | 270 | 87 | 32.2% |

### Violation Type Distribution Among Primary Violations

| violation_type | count | share |
| --- | --- | --- |
| false_unsupported_answer | 45 | 47.9% |
| title_based_overreach | 10 | 10.6% |
| unsupported_answer | 36 | 38.3% |
| unsupported_expansion | 3 | 3.2% |

### High-Salience Residual Failures

High-salience unsupported violations remained in 5 adjudicated primary-comparison records.

| model | high-salience unsupported violations |
| --- | --- |
| gemini_2_5_flash_lite | 3 |
| gemini_2_5_pro | 1 |
| openai_gpt_4o | 1 |

| model | question_id | paper_id | evidence | question_type | violation_type | factual_correctness |
| --- | --- | --- | --- | --- | --- | --- |
| openai_gpt_4o | paper_003_q1 | paper_003 | none | abstract_answerable | unsupported_answer | partially_correct |
| gemini_2_5_flash_lite | paper_003_q1 | paper_003 | none | abstract_answerable | title_based_overreach | partially_correct |
| gemini_2_5_flash_lite | paper_004_q2 | paper_004 | none | target_section_required | false_unsupported_answer | partially_correct |
| gemini_2_5_flash_lite | paper_005_q1_revised | paper_005 | none | abstract_answerable | false_unsupported_answer | partially_correct |
| gemini_2_5_pro | paper_003_q1 | paper_003 | none | abstract_answerable | title_based_overreach | partially_correct |

### Interpretation

The adjudicated primary comparison shows that explicit boundary language substantially reduced unsupported answering, but did not eliminate it. Residual failures under high salience are especially important because those prompts made the evidence boundary explicit. The post-adjudication results also confirm that unsupported answers are heterogeneous: some are false unsupported answers, some are unsupported answers or expansions, and some involve title-based overreach.

## Gemini-Family Comparison

Input file: `results/annotation_adjudicated/stage1_all810_annotations_main540_plus_gemini_2_5_family_adjudicated_v0_3.csv`

The Gemini-family comparison includes `gemini_2_5_flash_lite`, `gemini_2_5_flash`, and `gemini_2_5_pro`. These runs used `temperature=0.0`, `max_output_tokens=2048`, tool-off prompting, and no grounding, retrieval, browsing, URL context, code execution, or system prompts.

### Gemini EBC Label Counts

| model | n | compliant | violation | disclosed_expansion | unclear |
| --- | --- | --- | --- | --- | --- |
| gemini_2_5_flash | 90 | 89 | 1 | 0 | 0 |
| gemini_2_5_flash_lite | 90 | 76 | 14 | 0 | 0 |
| gemini_2_5_pro | 90 | 84 | 6 | 0 | 0 |

### Gemini Unsupported Violation Rates By Salience

| model | salience | unsupported n | violations | violation rate |
| --- | --- | --- | --- | --- |
| gemini_2_5_flash | low | 15 | 1 | 6.7% |
| gemini_2_5_flash | medium | 15 | 0 | 0.0% |
| gemini_2_5_flash | high | 15 | 0 | 0.0% |
| gemini_2_5_flash_lite | low | 15 | 7 | 46.7% |
| gemini_2_5_flash_lite | medium | 15 | 4 | 26.7% |
| gemini_2_5_flash_lite | high | 15 | 3 | 20.0% |
| gemini_2_5_pro | low | 15 | 4 | 26.7% |
| gemini_2_5_pro | medium | 15 | 1 | 6.7% |
| gemini_2_5_pro | high | 15 | 1 | 6.7% |

After adjudication, Gemini-family residual high-salience failures remained. Flash-Lite had 3 high-salience unsupported violations, and Gemini 2.5 Pro gained one additional high-salience violation relative to the pre-adjudication file.

## Claude-Family Default-Sampling Extension

Input file: `results/annotation_adjudicated/stage1_claude_family_default_sampling_with_fable_adjudicated_v0_3.csv`

This extension contains 360 records from Claude-family default-sampling runs: `anthropic_claude_haiku_4_5_temp_omitted`, `anthropic_claude_sonnet_5`, `anthropic_claude_opus_4_8_temp_omitted`, and `anthropic_claude_fable_5_temp_omitted`. Temperature was omitted, so these runs are not directly part of the temperature-controlled main table.

### Claude Default-Sampling EBC Label Counts By Model

| model | n | compliant | violation | disclosed_expansion | unclear |
| --- | --- | --- | --- | --- | --- |
| anthropic_claude_fable_5_temp_omitted | 90 | 77 | 4 | 9 | 0 |
| anthropic_claude_haiku_4_5_temp_omitted | 90 | 89 | 1 | 0 | 0 |
| anthropic_claude_opus_4_8_temp_omitted | 90 | 90 | 0 | 0 | 0 |
| anthropic_claude_sonnet_5 | 90 | 90 | 0 | 0 | 0 |

### Claude Default-Sampling Violation And Disclosed-Expansion Counts

| model | violation count | disclosed_expansion count | n |
| --- | --- | --- | --- |
| anthropic_claude_fable_5_temp_omitted | 4 | 9 | 90 |
| anthropic_claude_haiku_4_5_temp_omitted | 1 | 0 | 90 |
| anthropic_claude_opus_4_8_temp_omitted | 0 | 0 | 90 |
| anthropic_claude_sonnet_5 | 0 | 0 | 90 |

The disclosed-expansion pattern remains analytically useful, but adjudication narrowed it. Several Fable 5 outputs first labeled as disclosed expansion were adjudicated as compliant because they were refusals or title-scoped partial answers rather than actual external expansions.

## Second-Pass Validation And Adjudication

| metric | value |
| --- | --- |
| blind second-pass packet size | 355 |
| EBC_label percent agreement | 91.0% |
| EBC_label Cohen's kappa | 0.811 |
| EBC_label discrepancies adjudicated | 32 |
| adjudication final compliant | 31 |
| adjudication final violation | 1 |
| adjudication final disclosed_expansion | 0 |

The blind second-pass packet targeted likely disagreement and high-value review cases rather than sampling the full 1,260-row archive. The EBC-label percent agreement was 91.0% and Cohen's kappa was 0.811. All 32 EBC-label discrepancies were adjudicated using final adjudication fields only, not raw second-pass labels. The adjudicated outcomes among the 32 EBC disagreements were 31 compliant and 1 violation.

## All-Results Archive

Input file: `results/annotation_adjudicated/stage1_all1260_annotations_main540_plus_all_exploratory_and_gemini_2_5_family_adjudicated_v0_3.csv`

Total records: 1260

The all-results archive combines the main temperature-controlled comparison, the Claude-family default-sampling extension, and exploratory runs.

### Archive Model Categories

| model | records | archive category |
| --- | --- | --- |
| anthropic_claude_fable_5_temp_omitted | 90 | Claude default-sampling extension |
| anthropic_claude_haiku_4_5 | 90 | main temperature-controlled comparison |
| anthropic_claude_haiku_4_5_temp_omitted | 90 | Claude default-sampling extension |
| anthropic_claude_opus_4_8_temp_omitted | 90 | Claude default-sampling extension |
| anthropic_claude_sonnet_5 | 90 | Claude default-sampling extension |
| gemini_2_5_flash | 90 | main temperature-controlled comparison |
| gemini_2_5_flash_lite | 90 | main temperature-controlled comparison |
| gemini_2_5_pro | 90 | main temperature-controlled comparison |
| openai_gpt_4_1 | 90 | main temperature-controlled comparison |
| openai_gpt_4_1_mini | 90 | main temperature-controlled comparison |
| openai_gpt_4_1_nano | 90 | main temperature-controlled comparison |
| openai_gpt_4o | 90 | main temperature-controlled comparison |
| openai_gpt_4o_mini | 90 | main temperature-controlled comparison |
| openai_gpt_5_mini | 90 | exploratory |

### Supported vs Unsupported Records, All-Results Archive

| expected_support | records |
| --- | --- |
| not_supported | 630 |
| supported | 630 |

The main comparison is the temperature-controlled set used for the central Stage 1 claims. The Claude default-sampling runs are extensions because temperature was omitted. `openai_gpt_5_mini` remains exploratory because it required GPT-5-specific request settings, including omitted temperature and reasoning/output-token adjustments, which distinguish it from the main comparison.

## Qualitative Pattern Summary

| pattern | count in adjudicated all-results archive |
| --- | --- |
| unsupported factually correct or partial violations | 84 |
| false unsupported answers | 51 |
| title-based overreach | 10 |
| disclosed expansion | 9 |
| supported-condition direct answers | 583 |
| selective partial answers | 83 |

Unsupported but factually correct answers show that evidence-boundary compliance is not merely a matter of factual correctness. A model can provide a factually correct or partially correct answer while still violating the evidence boundary if the answer is not supported by the authorized evidence condition.

False unsupported answers combine evidentiary overreach with incorrect content. Title-based overreach occurs when a model infers content-specific claims from bibliographic or title-level cues rather than from the authorized evidence. Disclosed expansion is different from ordinary violation because the model explicitly signals that it is going beyond the provided text.

Supported-condition direct answers are usually compliant when correct and supported. Selective partial answers may also be compliant when the model answers only the supported part and withholds the unsupported part.

## Suggested Manuscript Language

After blind second-pass review and adjudication, the Stage 1 results suggest that evidence-boundary compliance is a separable dimension of document-grounded question answering. In unsupported conditions, models sometimes produced answers that were factually plausible, partially correct, or correct, but not warranted by the supplied text. This pattern indicates that the evaluation is not merely measuring factual accuracy; it is measuring whether the model respects the evidentiary boundary imposed by the task.

Increasing the salience of the evidence boundary substantially reduced unsupported answering. In the adjudicated primary comparison, unsupported-condition violations were most frequent under low-salience instructions and least frequent under high-salience instructions. However, high salience did not eliminate violations, indicating that explicit boundary language improves behavior for most but not all models and cases.

The adjudicated results also show model-level boundary sensitivity. Models differed in their tendency to refuse, answer, partially answer, or disclose expansion beyond the provided material. These differences appeared even though the task structure, evidence conditions, and salience manipulation were held constant within the primary comparison.

The Gemini-family results provide a third-provider replication under temperature-controlled, tool-off, grounding-off settings. The Gemini models followed the same broad salience-sensitive pattern, while still exhibiting model-level differences and residual high-salience failures after adjudication.

The Claude-family default-sampling extension should be interpreted separately from the temperature-controlled comparison. Because temperature was omitted for these runs, they are not directly comparable to the main table. Nevertheless, the extension identifies a useful qualitative distinction between silent unsupported answers and disclosed expansion beyond the provided evidence.

Taken together, the adjudicated Stage 1 results support a cautious interpretation: explicit evidence-boundary instructions can substantially improve compliance, but they do not fully solve the problem. The remaining failures matter because they occur in settings where the task explicitly restricts admissible evidence, suggesting that document-grounded QA systems may require evaluation criteria that distinguish answer correctness from evidence-boundary adherence.

## Limitations

The paper set is small, so the results should be treated as an initial controlled pilot rather than a broad benchmark. The salience manipulation is prompt-based, which improves reproducibility but does not exhaust the ways systems might express or enforce evidence boundaries in deployed settings.

Model availability and API settings differ across providers. The Claude default-sampling extension is not directly comparable to the temperature-controlled main runs because temperature was omitted. The GPT-5-mini exploratory run also involves reasoning/output-token settings that distinguish it from the main comparison.

The second-pass review was conducted on a targeted review packet rather than the full 1,260 rows. This improves adjudication effort on likely disagreements and high-value cases, but it should not be interpreted as a fully independent reannotation of the entire archive.

## Next Steps

Decide which adjudicated tables belong in the main text and which should move to the appendix. Preserve raw outputs and pre-adjudication annotation files for reproducibility. Optionally add a compact appendix describing the second-pass sampling strategy, agreement statistics, and adjudication procedure.
