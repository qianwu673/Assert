# Evidence-Boundary Compliance Reproducibility Package

This repository package accompanies the technical report:

**Beyond Correctness: A Controlled Evaluation of Evidence-Boundary Compliance in Large Language Models**

It allows readers to reproduce the reported Stage 1 tables, figures, and second-pass validation metrics from saved adjudicated annotations. It does **not** rerun model APIs.

## Scope

The main quantitative analysis is the 810-record primary temperature-controlled comparison:

- 5 papers
- 10 question IDs
- 3 evidence conditions: `full`, `partial`, `none`
- 3 boundary-salience conditions: `low`, `medium`, `high`
- 9 primary models
- 405 supported records and 405 unsupported records

The Claude default-sampling extension is included for qualitative and non-comparable model-family analysis. GPT-5-mini is retained only for transparency inside the all-results archive and as a separate extracted file under `excluded_exploratory/`. It is excluded from the main quantitative claims because it used exploratory request settings.

## What Is Included

- Adjudicated primary annotations.
- Adjudicated all-results archive.
- Claude default-sampling adjudicated annotations.
- Blind second-pass completed labels.
- Key linking second-pass rows to first-pass labels.
- Adjudicated second-pass discrepancy file.
- Primary item definitions.
- Salience prompt wrappers.
- Adjudicated master report.
- Current manuscript TEX draft.
- Reproduction scripts for tables, validation metrics, and figures.

## What Is Not Included

- API keys, `.env` files, credentials, or local machine paths.
- Full source-paper PDFs.
- Long source-paper excerpts.
- Raw JSONL model-output files. These are excluded from the public package because they may contain rendered prompts, evidence packets, provider metadata, and source-paper material. The reported tables and figures are reproduced from adjudicated annotations.

## Installation

Python 3.10+ is recommended.

```bash
pip install -r requirements.txt
```

The scripts use only the Python standard library, so this command should not install additional packages.

## Reproduce The Analysis

From the package root, run:

```bash
python scripts/validate_counts.py
python scripts/compute_main_tables.py
python scripts/compute_second_pass_metrics.py
python scripts/make_fig_salience.py
python scripts/make_fig_heatmap.py
```

Expected validation result:

```text
All reported manuscript counts reproduced exactly.
```

Generated outputs:

- `data/reports/reproduced_main_tables.md`
- `data/reports/reproduced_second_pass_metrics.md`
- `figures/stage1_salience_violation_rates.svg`
- `figures/stage1_model_by_salience_heatmap.svg`

## Key Reported Numbers

The validation script checks the following adjudicated values:

- Primary records: 810
- Supported / unsupported records: 405 / 405
- Unsupported violations: 94/405 = 23.2%
- Low salience: 67/135 = 49.6%
- Medium salience: 22/135 = 16.3%
- High salience: 5/135 = 3.7%
- Full evidence violations: 0/270
- Partial evidence violations: 7/270
- None evidence violations: 87/270
- High-salience residual failures: 5
- Second-pass packet size: 355
- `EBC_label` agreement: 91.0%
- Cohen's kappa: 0.811
- Adjudicated `EBC_label` disagreements: 32
- Final adjudication among disagreements: 31 compliant, 1 violation
- Claude Fable 5 disclosed-expansion count: 9

## Data Notes

See:

- `docs/data_dictionary.md`
- `docs/codebook_v0_3.md`
- `docs/model_aliases.md`
- `docs/annotation_guidelines.md`

## License

The reproduction code and package metadata are released under the MIT License. The annotation data are provided for research reproducibility. This package does not redistribute full copyrighted source papers.
