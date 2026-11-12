import csv
import logging
from pathlib import Path

from current_state import build_current_state

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def aggregate_daily_metrics(current_state):
    groups = {}

    for event in current_state.values():
        if event["status"] != "active":
            continue

        if not event.get("product_id"):
            logger.warning("Skipping event with missing product_id")
            continue

        if not isinstance(event.get("quantity"), int) or event["quantity"] < 0:
            logger.warning("Skipping event with invalid quantity: %s", event)
            continue

        if not isinstance(event.get("amount_minor"), int) or event["amount_minor"] < 0:
            logger.warning("Skipping event with invalid amount: %s", event)
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

    for input_file in input_files:
        if not input_file.exists():
            logger.error("Input file not found: %s", input_file)
            raise FileNotFoundError(f"Input file not found: {input_file}")

    logger.info("Building current state from %d input files", len(input_files))
    current_state = build_current_state(input_files)

    logger.info("Aggregating daily metrics")
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

    logger.info("Output rows: %d", len(metrics))
    logger.info("Saved: %s", output_file)


if __name__ == "__main__":
    main()