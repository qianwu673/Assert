# Tool-on EBC Reproducibility Package

This package contains a minimal public reproducibility bundle for the Tool-on Evidence-Boundary Compliance (EBC) experiments, including the ESR-check intervention. It includes selected records, aggregate audit outputs, human-labeled review sheets, prompt templates, and parser/prompt-building scripts.

Authorized evidence in this protocol is limited to the initial evidence packet plus snippets returned by the local authorized search tool. Memory, prior knowledge, browsing, open-web search, URL context, private source PDFs, extracted full source text, and unreturned corpus text are outside the evidence boundary.

## Aggregate Results

- **Full120** (tool-on full pilot): 120 total records, 119 substantively analyzable, 117 compliant, 2 violation, 1 invalid_or_unparseable.
- **ESR60** (ESR-check intervention): 60 total records, 60 analyzable, 60 compliant, 0 violation, 0 invalid.

## Which Columns Are Authoritative

- `full120_substantive_audit_human_labeled.csv`: use the **`final_*`** columns (`final_post_tool_EBC_label`, `final_repair_outcome`). The `human_*` columns are filled only for the 84 records that went through human review; the `final_*` columns merge human labels (where present) with preliminary labels (for the remaining 36 low-risk records) and are the columns the report is based on.
- `esr60_substantive_audit.csv`: the `preliminary_post_tool_EBC_label` column intentionally leaves the 34 tool-answer records as `needs_human_review`. The final ESR60 labels are obtained by joining with `esr60_human_review_sheet_all_checked.csv` on `record_id`; all 34 reviewed records resolved to `compliant` / `tool_repair_success`. The remaining 26 records (15 `direct_supported_from_initial`, 10 `compliant_withholding_without_tool`, 1 `failed_retrieval_honesty`) are labeled directly in the audit file.

## Checking Counts

Row counts:

```powershell
(Import-Csv .\data\derived\full120_substantive_audit_human_labeled.csv).Count   # 120
(Import-Csv .\data\derived\esr60_substantive_audit.csv).Count                   # 60
```

Full120 final labels (reproduces 117 / 2 / 1):

```powershell
Import-Csv .\data\derived\full120_substantive_audit_human_labeled.csv |
  Group-Object final_post_tool_EBC_label
```

ESR60 final labels (requires the join; reproduces 60 compliant):

```powershell
$audit  = Import-Csv .\data\derived\esr60_substantive_audit.csv
$review = Import-Csv .\data\derived\esr60_human_review_sheet_all_checked.csv
$rmap   = @{}; foreach ($r in $review) { $rmap[$r.record_id] = $r.human_post_tool_EBC_label }
$audit | ForEach-Object {
    if ($_.preliminary_post_tool_EBC_label -eq 'needs_human_review') { $rmap[$_.record_id] }
    else { $_.preliminary_post_tool_EBC_label }
} | Group-Object
```

A quick violation check that needs no join: every ESR60 record has `unsupported_without_tool = no`:

```powershell
Import-Csv .\data\derived\esr60_substantive_audit.csv | Group-Object unsupported_without_tool
```

Equivalent checks in Python:

```python
import csv
from collections import Counter

rows = list(csv.DictReader(open(
    "data/derived/full120_substantive_audit_human_labeled.csv", encoding="utf-8-sig")))
print(len(rows), Counter(r["final_post_tool_EBC_label"] for r in rows))
# 120 Counter({'compliant': 117, 'violation': 2, 'invalid_or_unparseable': 1})

audit = list(csv.DictReader(open(
    "data/derived/esr60_substantive_audit.csv", encoding="utf-8-sig")))
review = {r["record_id"]: r["human_post_tool_EBC_label"] for r in csv.DictReader(open(
    "data/derived/esr60_human_review_sheet_all_checked.csv", encoding="utf-8-sig"))}
final = [review.get(r["record_id"], r["preliminary_post_tool_EBC_label"])
         if r["preliminary_post_tool_EBC_label"] == "needs_human_review"
         else r["preliminary_post_tool_EBC_label"] for r in audit]
print(len(audit), Counter(final))
# 60 Counter({'compliant': 60})
```

Note: `esr60_substantive_audit.csv` begins with a UTF-8 BOM; use `encoding="utf-8-sig"` in Python (PowerShell's `Import-Csv` handles it automatically).

## Mapping Report Tables to Data Files

| Report table | Source of the numbers |
| --- | --- |
| Table 3 (overall EBC outcomes) | `full120_substantive_audit_human_labeled.csv`, `final_post_tool_EBC_label` |
| Table 4 (tool-call by model) | same file, `tool_called` grouped by `model_slot` |
| Table 5 (optional-tool insufficient rate) | same file, filter `tool_condition = optional_tool` and `tool_needed = yes` |
| Table 6 (required-if-insufficient compliance) | same file, filter `tool_condition = required_if_insufficient` and `tool_needed = yes` |
| Table 7 (repair outcomes) | same file, `final_repair_outcome` |
| Table 8 (ESR-check outcomes) | `esr60_substantive_audit.csv` joined with `esr60_human_review_sheet_all_checked.csv` |
| Table 9, baseline row | `full120_substantive_audit_human_labeled.csv`, optional-tool insufficient subset (45 = 31 tool + 12 withhold + 2 violation) |
| Table 9, ESR-check row | `esr60_substantive_audit.csv`, insufficient subset (45 = 35 tool + 10 withhold; 35 = 34 `tool_repair_success` after review + 1 `failed_retrieval_honesty`) |

Human review of answer-vs-evidence support used only the authorized evidence visible to the model (initial packet and returned snippets), never the full papers or outside knowledge.

## Exclusions

Full PDFs, `private_sources/`, extracted `source_texts/`, authorized-corpus `chunks/`, `.env` files, API keys, and other private source material are intentionally excluded. This package is intended for public release and should not redistribute full source papers or credentials.
