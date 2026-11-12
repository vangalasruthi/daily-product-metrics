import csv
from pathlib import Path

from current_state import build_current_state


def aggregate_daily_metrics(current_state):
    groups = {}

    for event in current_state.values():
        if event["status"] != "active":
            continue

        key = (event["business_date"], event["product_id"])

        if key not in groups:
            groups[key] = {
                "business_date": event["business_date"],
                "product_id": event["product_id"],
                "active_transaction_count": 0,
                "units_sold": 0,
                "sales_amount_minor": 0,
            }

        groups[key]["active_transaction_count"] += 1
        groups[key]["units_sold"] += event["quantity"]
        groups[key]["sales_amount_minor"] += event["amount_minor"]

    return [groups[key] for key in sorted(groups)]


def main():
    project_dir = Path(__file__).resolve().parent.parent

    input_files = [
        project_dir / "data" / "input" / "batch_001.jsonl",
        project_dir / "data" / "input" / "batch_002.jsonl",
    ]

    current_state = build_current_state(input_files)
    metrics = aggregate_daily_metrics(current_state)

    output_dir = project_dir / "data" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "daily_product_metrics.csv"

    fieldnames = [
        "business_date",
        "product_id",
        "active_transaction_count",
        "units_sold",
        "sales_amount_minor",
    ]

    with output_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(metrics)

    print(f"Output rows: {len(metrics)}")
    print(f"Saved: {output_file}")


if __name__ == "__main__":
    main()