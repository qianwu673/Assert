# Data Dictionary

This package reproduces the reported Stage 1 tables from adjudicated annotation CSV files. The main file is:

`data/annotations/stage1_primary810_annotations_adjudicated_v0_3.csv`

The all-results archive is:

`data/annotations/stage1_all1260_annotations_adjudicated_v0_3.csv`

## Annotation CSV Columns

| Column | Meaning |
| --- | --- |
| `record_id` | Unique row identifier for one model response. |
| `model_name` | Exact model alias used in analysis. See `docs/model_aliases.md`. |
| `paper_id` | Paper identifier, such as `paper_003`. |
| `question_id` | Question identifier, such as `paper_003_q1`. |
| `question_type` | `abstract_answerable` or `target_section_required`. |
| `question` | Target question asked of the model. |
| `evidence_condition` | `full`, `partial`, or `none`. |
| `salience_condition` | `low`, `medium`, or `high`. |
| `expected_support` | `supported` or `not_supported` for the assigned item/evidence condition. |
| `api_called` | Whether a real provider API was called for the original model output. |
| `error` | Provider or runner error field, empty for successful records. |
| `model_response` | Model response text. |
| `answer_status` | Response-form code. See `docs/codebook_v0_3.md`. |
| `EBC_label` | Main evidence-boundary compliance label. |
| `EBA_score` | Evidence-boundary awareness score, 0 to 3. |
| `refusal_type` | Refusal subtype. |
| `violation_type` | Evidence-boundary violation subtype. |
| `factual_correctness` | Factual correctness of substantive answer content. |
| `answerability_error` | Design or answerability flag, if used. |
| `support_note` | Short annotation note about evidence support. |
| `annotator_note` | Short annotation note about the response. |
| `_source_annotation_file` | Source annotation file used when constructing the aggregate. |
| `gold_answer` | Human gold answer or concise target answer. |
| `effective_support` | Effective support status used for analysis. |
| `analysis_flag` | Analysis grouping flag, when present. |
| `adjudicated` | `true` when final labels were applied through adjudication. |
| `adjudication_note` | Short note explaining adjudication, when present. |

## Second-Pass CSV Columns

| Column | Meaning |
| --- | --- |
| `second_pass_id` | Identifier for one blind second-pass review row. |
| `selection_reason` | Semicolon-separated reason(s) the row was selected. |
| `original_record_id` | Original annotation `record_id`; present in key and adjudication files. |
| `first_pass_EBC_label` | First-pass EBC label. |
| `second_pass_EBC_label` | Blind second-pass EBC label. |
| `final_EBC_label` | Final adjudicated EBC label for discrepant rows. |
| `accepted_source` | Which annotation source was accepted during adjudication, when recorded. |
| `final_*` columns | Final adjudicated codes for discrepant rows. |

## Primary Comparison

The primary comparison is the 810-record temperature-controlled dataset in `stage1_primary810_annotations_adjudicated_v0_3.csv`. GPT-5-mini is exploratory and excluded from main quantitative claims. Claude default-sampling runs are included only as a qualitative/non-comparable extension.
