# Tool-on EBC Reproducibility Package

This package contains a minimal public reproducibility bundle for the Tool-on Evidence-Boundary Compliance experiments. It includes selected records, aggregate audit outputs, human-labeled review sheets when available, prompt templates, and parser/prompt-building scripts.

Authorized evidence in this protocol is limited to the initial evidence packet plus snippets returned by the local authorized search tool. Memory, prior knowledge, browsing, open-web search, URL context, private source PDFs, extracted full source text, and unreturned corpus text are outside the evidence boundary.

## Aggregate Results

- Full120: 120 total records, 119 analyzable, 117 compliant, 2 violation, 1 invalid.
- ESR60: 60 total records, 60 analyzable, 60 compliant, 0 violation.

## Checking Counts

Aggregate counts can be checked from the included CSV files with a local CSV reader. For example, in PowerShell:

```powershell
(Import-Csv .\data\derived\full120_substantive_audit_human_labeled.csv).Count
(Import-Csv .\data\derived\esr60_substantive_audit.csv).Count
```

Label counts can be checked by grouping the relevant label columns, for example:

```powershell
Import-Csv .\data\derived\full120_substantive_audit_human_labeled.csv | Group-Object human_post_tool_EBC_label
Import-Csv .\data\derived\esr60_substantive_audit.csv | Group-Object preliminary_post_tool_EBC_label
```

## Exclusions

Full PDFs, `private_sources/`, extracted `source_texts/`, authorized-corpus `chunks/`, `.env` files, API keys, and other private source material are intentionally excluded. This package is intended for public GitHub release and should not redistribute full source papers or credentials.
