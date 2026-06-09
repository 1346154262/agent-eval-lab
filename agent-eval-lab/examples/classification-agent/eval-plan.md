# Classification Agent Evaluation Plan

## Tested Agent

- Name: sample-ticket-classifier
- Business task: classify support tickets into billing, technical, account, or other.
- Output contract: JSON with `category` and `confidence`.

## Dataset

- Dataset version: sample-v1
- Case count: 4
- Coverage strategy: common billing, technical, account, and ambiguous other cases.

## Metrics

- L1: parseability, format compliance, required-field completeness.
- L2: classification accuracy.
- L3: route-blocking business-rule compliance.

## Release Decision

Pass when all L1 checks pass and classification accuracy is at least 0.75.
