# Agent Eval Lab

English | [简体中文](README.zh-CN.md)

Agent Eval Lab is a Harness-style evaluation lab for business agents. It uses a strong coding agent, such as Codex or ClaudeCode, as the Harness Builder that designs evaluation plans, creates golden datasets, writes evaluator prompts, summarizes results, and recommends improvements.

The core idea is to move fast-changing business evaluation logic out of scattered scripts and into prompts, rubrics, schemas, and reusable templates. Python scripts in this repository stay narrow: they validate datasets and summarize recorded results.

## What This Repository Contains

- A Codex-compatible skill for building agent evaluation harnesses.
- A three-level metric taxonomy for agent evaluation.
- Templates for evaluation plans, evaluator-agent prompts, judge rubrics, datasets, result records, and error taxonomies.
- A small classification-agent example.
- Lightweight scripts for dataset validation and result summarization.

## First-Version Scope

This repository does not call OpenAI, Anthropic, Claude, or other model APIs. It is designed for task-pack evaluation, human or semi-automatic scoring, and report generation. API runners can be added later without changing the core folder model.

## Quick Start

Install dependencies:

```bash
python -m pip install -e ".[dev]"
```

Validate the example dataset:

```bash
python agent-eval-lab/scripts/validate_dataset.py agent-eval-lab/examples/classification-agent/dataset.yaml
```

Summarize the example results:

```bash
python agent-eval-lab/scripts/summarize_results.py agent-eval-lab/examples/classification-agent/results.yaml --markdown report.generated.md --json report.generated.json
```

## Harness Workflow

1. Define the tested agent, business task, output contract, and release risk.
2. Draft an evaluation plan before writing runner code.
3. Build a small golden dataset, usually 20 to 55 cases.
4. Select L1, L2, and L3 metrics.
5. Write an Evaluator Agent prompt.
6. Run or guide evaluation.
7. Summarize failures, evidence, and recommended improvements.
8. Use human spot checks for high-risk or judge-sensitive cases.

## License

MIT
