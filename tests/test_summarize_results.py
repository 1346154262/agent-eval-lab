from pathlib import Path

from importlib.machinery import SourceFileLoader


MODULE_PATH = Path(__file__).resolve().parents[1] / "agent-eval-lab" / "scripts" / "summarize_results.py"
summarize_results = SourceFileLoader("summarize_results", str(MODULE_PATH)).load_module()


def test_summarize_counts_passed_cases_and_errors():
    data = {
        "dataset_version": "v1",
        "agent": "agent-a",
        "results": [
            {"case_id": "one", "passed": True, "scores": {"l1": {"format": 1.0}}, "errors": []},
            {
                "case_id": "two",
                "passed": False,
                "scores": {"l1": {"format": 1.0}, "l2": {"accuracy": 0.0}},
                "errors": ["wrong_classification"],
            },
        ],
    }

    summary = summarize_results.summarize(data)

    assert summary["case_count"] == 2
    assert summary["passed_count"] == 1
    assert summary["failed_count"] == 1
    assert summary["error_counts"] == {"wrong_classification": 1}
    assert summary["metric_averages"]["l1.format"] == 1.0
    assert summary["metric_averages"]["l2.accuracy"] == 0.0


def test_markdown_report_contains_key_sections():
    summary = {
        "agent": "agent-a",
        "dataset_version": "v1",
        "case_count": 1,
        "passed_count": 1,
        "failed_count": 0,
        "error_counts": {},
        "metric_averages": {"l1.format": 1.0},
    }

    markdown = summarize_results.to_markdown(summary)

    assert "# Agent Evaluation Report" in markdown
    assert "- Agent: agent-a" in markdown
    assert "l1.format" in markdown
