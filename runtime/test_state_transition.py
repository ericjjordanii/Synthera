from runtime.state_transition import TransitionRequest, validate_transition, verify_consistency


def request(previous: str, new: str, event_type: str) -> TransitionRequest:
    return TransitionRequest(
        transaction_id="TX-TEST-0001",
        project_id="SYN-P001",
        entity_id="SYN-P001-L001",
        correlation_id="RUN-TEST-0001",
        actor_id="SYN-P001-A001",
        expected_previous_state=previous,
        requested_new_state=new,
        event_type=event_type,
        occurred_at="2026-08-13T00:00:00-05:00",
    )


def test_valid_transition_is_pending_before_persistence():
    result = validate_transition("READY_TO_LEARN", request("READY_TO_LEARN", "LEARNING", "lesson_started"))
    assert result.status == "PENDING"


def test_stale_expected_state_is_rejected():
    result = validate_transition("LEARNING", request("READY_TO_LEARN", "LEARNING", "lesson_started"))
    assert result.status == "REJECTED"


def test_invalid_lifecycle_jump_is_rejected():
    result = validate_transition("LEARNING", request("LEARNING", "PUBLISHED", "published"))
    assert result.status == "REJECTED"


def test_production_unlock_requires_correct_event_type():
    result = validate_transition("PROFICIENCY_PASSED", request("PROFICIENCY_PASSED", "PRODUCTION_UNLOCKED", "lesson_started"))
    assert result.status == "REJECTED"


def test_consistency_mismatch_requires_recovery():
    result = verify_consistency("PROFICIENCY_PASSED", "LEARNING", "EVT-3", "EVT-2")
    assert result.status == "RECOVERY_REQUIRED"


def test_consistent_event_and_state_commit():
    result = verify_consistency("PROFICIENCY_PASSED", "PROFICIENCY_PASSED", "EVT-3", "EVT-3")
    assert result.status == "COMMITTED"
