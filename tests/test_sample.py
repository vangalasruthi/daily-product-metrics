import json
from pathlib import Path


def test_first_batch_sample():
    project_dir = Path(__file__).resolve().parent.parent
    input_file = project_dir / "data" / "input" / "batch_001.jsonl"

    with input_file.open(encoding="utf-8-sig") as file:
        records = [
            json.loads(line)
            for line in file
            if line.strip()
        ]

    assert len(records) == 2
    assert sum(record["amount_minor"] for record in records) == 15000