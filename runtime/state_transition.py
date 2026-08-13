from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class TransitionRequest:
    transaction_id: str
    project_id: str
    entity_id: str
    correlation_id: str
    actor_id: str
    expected_previous_state: str
    requested_new_state: str
    event_type: str
    occurred_at: str
    reason: Optional[str] = None


@dataclass(frozen=True)
class TransitionResult:
    status: str
    message: str


LESSON_TRANSITIONS = {
    "PLANNED": {"READY_TO_LEARN"},
    "READY_TO_LEARN": {"LEARNING"},
    "LEARNING": {"ASSESSMENT_REQUIRED", "PROFICIENCY_PASSED"},
    "ASSESSMENT_REQUIRED": {"LEARNING", "PROFICIENCY_PASSED"},
    "PROFICIENCY_PASSED": {"PRODUCTION_UNLOCKED"},
    "PRODUCTION_UNLOCKED": {"PRODUCTION_IN_PROGRESS"},
    "PRODUCTION_IN_PROGRESS": {"PRODUCTION_COMPLETE"},
    "PRODUCTION_COMPLETE": {"PUBLISHED"},
}


def validate_transition(current_state: str, request: TransitionRequest) -> TransitionResult:
    if current_state != request.expected_previous_state:
        return TransitionResult(
            "REJECTED",
            "Current state does not match expected_previous_state.",
        )

    allowed = LESSON_TRANSITIONS.get(current_state, set())
    if request.requested_new_state not in allowed:
        return TransitionResult(
            "REJECTED",
            "Requested transition is not permitted by the lesson lifecycle.",
        )

    if request.requested_new_state == "PRODUCTION_UNLOCKED" and request.event_type != "production_unlocked":
        return TransitionResult(
            "REJECTED",
            "Production unlock requires a production_unlocked event.",
        )

    return TransitionResult("PENDING", "Transition is valid and ready for persistence.")


def verify_consistency(event_new_state: str, state_current_state: str, event_id: str, source_event_id: str) -> TransitionResult:
    if event_new_state != state_current_state:
        return TransitionResult("RECOVERY_REQUIRED", "Event and current state disagree.")
    if event_id != source_event_id:
        return TransitionResult("RECOVERY_REQUIRED", "Current state references the wrong source event.")
    return TransitionResult("COMMITTED", "Event history and current state are consistent.")
