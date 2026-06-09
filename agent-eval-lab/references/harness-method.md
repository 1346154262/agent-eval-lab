# Harness Method

Use a strong agent as the Harness Builder. The Harness Builder owns evaluation-plan design, dataset construction support, evaluator-prompt writing, metric selection, result analysis, and improvement recommendations.

Humans own ground-truth labeling, plan approval, spot checks, and final release decisions.

Prefer prompt-based evaluation logic when business rules change quickly. Keep code for repeatable mechanics: schema validation, aggregation, and report generation.
