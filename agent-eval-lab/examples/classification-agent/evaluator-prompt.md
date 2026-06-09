# Sample Classification Evaluator Prompt

Evaluate each support-ticket classification result against the dataset ground truth.

Required tested-agent output:

```json
{"category": "billing|technical|account|other", "confidence": 0.0}
```

Score L1 format fields first. Then score L2 classification accuracy. Mark L3 route-blocking compliance as failed when the wrong category would send the ticket to the wrong business team.

Return final JSON result records only.
