from pathlib import Path

from importlib.machinery import SourceFileLoader


MODULE_PATH = Path(__file__).resolve().parents[1] / "agent-eval-lab" / "scripts" / "validate_dataset.py"
validate_dataset = SourceFileLoader("validate_dataset", str(MODULE_PATH)).load_module()


def test_valid_dataset_has_no_errors():
    dataset = {
        "version": "v1",
        "cases": [
            {
                "id": "case-001",
                "input": "hello",
                "expected": {"category": "other"},
                "metrics": ["format_compliance"],
                "difficulty": "easy",
                "boundary": "common",
            }
        ],
    }

    assert validate_dataset.validate_dataset(dataset) == []


def test_duplicate_case_ids_are_reported():
    dataset = {
        "version": "v1",
        "cases": [
            {
                "id": "case-001",
                "input": "hello",
                "expected": {"category": "other"},
                "metrics": ["format_compliance"],
                "difficulty": "easy",
                "boundary": "common",
            },
            {
                "id": "case-001",
                "input": "again",
                "expected": {"category": "other"},
                "metrics": ["format_compliance"],
                "difficulty": "easy",
                "boundary": "common",
            },
        ],
    }

    assert "duplicate case id: case-001" in validate_dataset.validate_dataset(dataset)


def test_invalid_difficulty_is_reported():
    dataset = {
        "version": "v1",
        "cases": [
            {
                "id": "case-001",
                "input": "hello",
                "expected": {"category": "other"},
                "metrics": ["format_compliance"],
                "difficulty": "extreme",
                "boundary": "common",
            }
        ],
    }

    assert "case-001: invalid difficulty: extreme" in validate_dataset.validate_dataset(dataset)
