import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from daily_metrics import aggregate_daily_metrics


def test_skips_missing_product_id():
    current_state = {
        "txn_1": {
            "status": "active",
            "business_date": "2026-11-10",
            "product_id": "",
            "quantity": 1,
            "amount_minor": 12000,
        }
    }

    metrics = aggregate_daily_metrics(current_state)
    assert metrics == []


def test_skips_negative_quantity():
    current_state = {
        "txn_1": {
            "status": "active",
            "business_date": "2026-11-10",
            "product_id": "product_001",
            "quantity": -1,
            "amount_minor": 12000,
        }
    }

    metrics = aggregate_daily_metrics(current_state)
    assert metrics == []


def test_skips_negative_amount():
    current_state = {
        "txn_1": {
            "status": "active",
            "business_date": "2026-11-10",
            "product_id": "product_001",
            "quantity": 1,
            "amount_minor": -12000,
        }
    }

    metrics = aggregate_daily_metrics(current_state)
    assert metrics == []


def test_skips_non_active_status():
    current_state = {
        "txn_1": {
            "status": "cancelled",
            "business_date": "2026-11-10",
            "product_id": "product_001",
            "quantity": 1,
            "amount_minor": 12000,
        }
    }

    metrics = aggregate_daily_metrics(current_state)
    assert metrics == []


def test_handles_multiple_products():
    current_state = {
        "txn_1": {
            "status": "active",
            "business_date": "2026-11-10",
            "product_id": "product_001",
            "quantity": 1,
            "amount_minor": 12000,
        },
        "txn_2": {
            "status": "active",
            "business_date": "2026-11-10",
            "product_id": "product_002",
            "quantity": 2,
            "amount_minor": 24000,
        },
    }

    metrics = aggregate_daily_metrics(current_state)
    assert len(metrics) == 2
    assert metrics[0]["product_id"] == "product_001"
    assert metrics[1]["product_id"] == "product_002"