import csv
from pathlib import Path


def read_csv_rows(path):
    with path.open(newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def test_generated_output_matches_expected():
    project_dir = Path(__file__).resolve().parent.parent

    actual_file = (
        project_dir / "data" / "output" / "daily_product_metrics.csv"
    )
    expected_file = (
        project_dir / "data" / "expected" / "batch_002_expected.csv"
    )

    assert actual_file.exists(), (
        "Output file missing. Run python src/daily_metrics.py first."
    )
    assert read_csv_rows(actual_file) == read_csv_rows(expected_file)