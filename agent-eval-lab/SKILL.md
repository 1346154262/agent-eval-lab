---
name: agent-eval-lab
description: Use when Codex needs to evaluate, compare, benchmark, validate, or build a Harness-style test workflow for agents such as Codex, Claude, ClaudeCode, coding agents, business task agents, classification agents, extraction agents, or content-generation agents. Guides a strong agent to design evaluation plans, golden datasets, evaluator prompts, L1/L2/L3 metrics, LLM-as-Judge rubrics, result schemas, error taxonomies, and reports while keeping deterministic code limited to validation and summarization.
---

# Agent Eval Lab

Use a strong agent as the Harness Builder for business-agent evaluation. The Harness Builder designs the evaluation plan, creates or reviews the golden dataset, writes the Evaluator Agent prompt, selects metrics, analyzes results, and proposes improvements.

## Workflow

1. Identify the tested agent, business task, output contract, and release risk.
2. Draft an evaluation plan before writing runner code. Use `templates/eval-plan-template.md`.
3. Build a small golden dataset, usually 20 to 55 cases. Read `references/dataset-guidelines.md`.
4. Select metrics from `references/metric-taxonomy.md`.
5. Write or adapt the Evaluator Agent prompt using `templates/evaluator-agent-prompt.md`.
6. Define result fields and error categories using `templates/result-schema.yaml` and `templates/error-taxonomy.yaml`.
7. Run or guide the evaluation.
8. Summarize scores, failure clusters, evidence, and recommended prompt or agent changes.
9. Require human spot checks for high-risk, borderline, or judge-sensitive cases.

## Design Rules

- Keep business-specific evaluation logic in prompts, rubrics, schemas, and datasets.
- Use scripts only for deterministic validation, aggregation, and report generation.
- Do not call model APIs unless the user explicitly asks to add an API runner.
- Do not claim LLM-as-Judge is fully objective.
- Preserve reproducibility by versioning datasets, prompts, rubrics, schemas, raw results, and reports.

## Reference Map

- Harness method: `references/harness-method.md`
- Metrics: `references/metric-taxonomy.md`
- Dataset design: `references/dataset-guidelines.md`
- Judge design: `references/llm-as-judge.md`
- Tested-agent calling: `references/tested-agent-calling.md`
- Report structure: `references/report-template.md`

## Scripts

- Validate a dataset:
  `python agent-eval-lab/scripts/validate_dataset.py <dataset.yaml>`

- Summarize results:
  `python agent-eval-lab/scripts/summarize_results.py <results.yaml> --markdown report.md --json report.json`
