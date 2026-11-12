from pathlib import Path

from src.current_state import build_current_state


def test_update_and_reversal():
    project_dir = Path(__file__).resolve().parent.parent
    input_files = [
        project_dir / "data" / "input" / "batch_001.jsonl",
        project_dir / "data" / "input" / "batch_002.jsonl",
    ]

    current_state = build_current_state(input_files)

    assert len(current_state) == 2
    assert current_state["txn_001"]["version"] == 2
    assert current_state["txn_001"]["amount_minor"] == 12000
    assert current_state["txn_002"]["version"] == 2
    assert current_state["txn_002"]["status"] == "reversed"

    active_events = [
        event
        for event in current_state.values()
        if event["status"] == "active"
    ]

    assert len(active_events) == 1
    assert sum(event["amount_minor"] for event in active_events) == 12000


def test_replay_and_out_of_order_batches():
    project_dir = Path(__file__).resolve().parent.parent
    batch_1 = project_dir / "data" / "input" / "batch_001.jsonl"
    batch_2 = project_dir / "data" / "input" / "batch_002.jsonl"

    expected_state = build_current_state([batch_1, batch_2])

    replayed_state = build_current_state(
        [batch_1, batch_2, batch_1, batch_2]
    )
    out_of_order_state = build_current_state([batch_2, batch_1])

    assert replayed_state == expected_state
    assert out_of_order_state == expected_state