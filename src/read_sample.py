import json
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
input_file = project_dir / "data" / "input" / "batch_001.jsonl"

record_count = 0
total_amount_minor = 0

with input_file.open(encoding="utf-8-sig") as file:
    for line_number, line in enumerate(file, start=1):
        if not line.strip():
            continue

        record = json.loads(line)
        record_count += 1
        total_amount_minor += record["amount_minor"]
        print(f"Line {line_number}: {record['event_id']}, amount: {record['amount_minor']}")

print(f"Total records: {record_count}")
print(f"Total amount in paise: {total_amount_minor}")