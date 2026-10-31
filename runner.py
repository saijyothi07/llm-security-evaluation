"""Load the dataset, evaluate the detector, and write a JSON report."""

import json
from pathlib import Path

from .detector import predict
from .metrics import calculate_metrics

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "prompts.jsonl"
REPORT_PATH = ROOT / "evaluation_report.json"


def load_dataset(path: Path = DATA_PATH) -> list[dict]:
    rows = []
    with path.open(encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_number}") from exc
            if not {"id", "text", "label"} <= row.keys():
                raise ValueError(f"Line {line_number} must contain id, text, label")
            if row["label"] not in (0, 1):
                raise ValueError(f"Line {line_number}: label must be 0 or 1")
            rows.append(row)
    if not rows:
        raise ValueError("Dataset is empty")
    return rows


def main() -> None:
    rows = load_dataset()
    labels = [row["label"] for row in rows]
    predictions = [predict(row["text"]) for row in rows]
    metrics = calculate_metrics(labels, predictions)

    results = [
        {
            "id": row["id"],
            "label": row["label"],
            "prediction": prediction,
            "correct": row["label"] == prediction,
        }
        for row, prediction in zip(rows, predictions)
    ]
    report = {"metrics": metrics, "results": results}
    REPORT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print("LLM Security Evaluation — rule-based baseline")
    for key, value in metrics.items():
        print(f"{key}: {value}")
    print(f"\nDetailed report: {REPORT_PATH}")


if __name__ == "__main__":
    main()
