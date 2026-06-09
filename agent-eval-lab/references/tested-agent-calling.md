# Tested-Agent Calling

Evaluator prompts should explicitly define how to call the tested agent or tool. Include parameter construction rules, required fields, and output expectations.

For batch evaluation, prefer no retries unless the evaluation plan explicitly measures retry behavior. Ask the evaluator to output final JSON only to reduce token use and parsing failures.

Record tool-call failures separately from answer-quality failures.
