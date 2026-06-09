#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


REQUIRED_CASE_FIELDS = {"id", "input", "expected", "metrics", "difficulty", "boundary"}
ALLOWED_DIFFICULTY = {"easy", "medium", "hard"}


def load_data(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return yaml.safe_load(text)


def validate_dataset(dataset: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    cases = dataset.get("cases")
    if not isinstance(cases, list):
        return ["dataset must contain a cases list"]

    seen_ids: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"case at index {index} must be an object")
            continue

        case_id = str(case.get("id", f"index-{index}"))
        missing = sorted(REQUIRED_CASE_FIELDS - set(case))
        for field in missing:
            errors.append(f"{case_id}: missing required field: {field}")

        if case_id in seen_ids:
            errors.append(f"duplicate case id: {case_id}")
        seen_ids.add(case_id)

        metrics = case.get("metrics")
        if "metrics" in case and not isinstance(metrics, list):
            errors.append(f"{case_id}: metrics must be a list")

        difficulty = case.get("difficulty")
        if "difficulty" in case and difficulty not in ALLOWED_DIFFICULTY:
            errors.append(f"{case_id}: invalid difficulty: {difficulty}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an agent evaluation dataset.")
    parser.add_argument("dataset", type=Path)
    args = parser.parse_args()

    errors = validate_dataset(load_data(args.dataset))
    if errors:
        for error in errors:
            print(error)
        return 1

    print(f"valid dataset: {args.dataset}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
