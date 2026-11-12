import json
from pathlib import Path


def build_current_state(input_files):
    current_state = {}

    for input_file in input_files:
        with input_file.open(encoding="utf-8-sig") as file:
            for line in file:
                if not line.strip():
                    continue

                event = json.loads(line)
                transaction_id = event["transaction_id"]
                previous = current_state.get(transaction_id)

                if previous is None or event["version"] > previous["version"]:
                    current_state[transaction_id] = event

    return current_state


def main():
    project_dir = Path(__file__).resolve().parent.parent

    input_files = [
        project_dir / "data" / "input" / "batch_001.jsonl",
        project_dir / "data" / "input" / "batch_002.jsonl",
    ]

    current_state = build_current_state(input_files)
    total_amount_minor = 0
    active_count = 0

    for transaction_id, event in sorted(current_state.items()):
        print(
            f"{transaction_id}: version={event['version']}, "
            f"status={event['status']}, amount={event['amount_minor']}"
        )

        if event["status"] == "active":
            active_count += 1
            total_amount_minor += event["amount_minor"]

    print(f"Active transactions: {active_count}")
    print(f"Active sales in paise: {total_amount_minor}")


if __name__ == "__main__":
    main()