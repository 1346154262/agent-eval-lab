#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml


def load_data(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return yaml.safe_load(text)


def summarize(data: dict[str, Any]) -> dict[str, Any]:
    results = data.get("results", [])
    error_counts: Counter[str] = Counter()
    metric_values: dict[str, list[float]] = defaultdict(list)

    for result in results:
        for error in result.get("errors", []):
            error_counts[str(error)] += 1

        for group, metrics in result.get("scores", {}).items():
            if not isinstance(metrics, dict):
                continue
            for metric, value in metrics.items():
                if isinstance(value, int | float):
                    metric_values[f"{group}.{metric}"].append(float(value))

    metric_averages = {
        metric: round(sum(values) / len(values), 4)
        for metric, values in sorted(metric_values.items())
        if values
    }

    passed_count = sum(1 for result in results if result.get("passed") is True)
    case_count = len(results)

    return {
        "agent": data.get("agent", "unknown"),
        "dataset_version": data.get("dataset_version", "unknown"),
        "case_count": case_count,
        "passed_count": passed_count,
        "failed_count": case_count - passed_count,
        "error_counts": dict(sorted(error_counts.items())),
        "metric_averages": metric_averages,
    }


def to_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# Agent Evaluation Report",
        "",
        "## Summary",
        "",
        f"- Agent: {summary['agent']}",
        f"- Dataset version: {summary['dataset_version']}",
        f"- Cases: {summary['case_count']}",
        f"- Passed cases: {summary['passed_count']}",
        f"- Failed cases: {summary['failed_count']}",
        "",
        "## Metric Averages",
        "",
    ]

    for metric, value in summary["metric_averages"].items():
        lines.append(f"- {metric}: {value}")

    lines.extend(["", "## Failure Clusters", ""])

    if summary["error_counts"]:
        for error, count in summary["error_counts"].items():
            lines.append(f"- {error}: {count}")
    else:
        lines.append("- No failures recorded.")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize agent evaluation results.")
    parser.add_argument("results", type=Path)
    parser.add_argument("--markdown", type=Path)
    parser.add_argument("--json", dest="json_path", type=Path)
    args = parser.parse_args()

    summary = summarize(load_data(args.results))
    markdown = to_markdown(summary)

    if args.markdown:
        args.markdown.write_text(markdown, encoding="utf-8")
    else:
        print(markdown)

    if args.json_path:
        args.json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
