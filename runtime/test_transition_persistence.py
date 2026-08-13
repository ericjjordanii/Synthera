from runtime.state_transition import TransitionRequest
from runtime.transition_persistence import TransitionExecutor


class FakeAdapter:
    def __init__(self, fail_state_writes=0):
        self.fail_state_writes = fail_state_writes
        self.events = []
        self.state = None
        self.state_write_attempts = 0

    def append_event(self, event):
        self.events.append(event)

    def write_state(self, state):
        self.state_write_attempts += 1
        if self.state_write_attempts <= self.fail_state_writes:
            raise RuntimeError("temporary write failure")
        self.state = state

    def read_latest_event(self, entity_id):
        return self.events[-1]

    def read_state(self, entity_id):
        return self.state


def request():
    return TransitionRequest(
        transaction_id="TX-TEST",
        project_id="SYN-P001",
        entity_id="SYN-P001-L002",
        correlation_id="RUN-TEST",
        actor_id="SYN-P001-A001",
        expected_previous_state="PROFICIENCY_PASSED",
        requested_new_state="PRODUCTION_UNLOCKED",
        event_type="production_unlocked",
        occurred_at="2026-08-13T20:00:00-05:00",
    )


def state():
    return {
        "current_state": "PROFICIENCY_PASSED",
        "source_event_id": "EVT-OLD",
    }


def test_retry_repairs_partial_write_without_duplicate_event():
    adapter = FakeAdapter(fail_state_writes=1)
    result = TransitionExecutor(adapter).execute(state(), request(), "EVT-NEW")
    assert result.status == "COMMITTED"
    assert len(adapter.events) == 1
    assert adapter.state_write_attempts == 2
    assert adapter.state["current_state"] == "PRODUCTION_UNLOCKED"
    assert adapter.state["source_event_id"] == "EVT-NEW"


def test_unrecoverable_state_write_requires_recovery():
    adapter = FakeAdapter(fail_state_writes=5)
    result = TransitionExecutor(adapter, max_state_write_attempts=3).execute(state(), request(), "EVT-NEW")
    assert result.status == "RECOVERY_REQUIRED"
    assert len(adapter.events) == 1
    assert adapter.state_write_attempts == 3
