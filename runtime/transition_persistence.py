from copy import deepcopy
from dataclasses import dataclass
from typing import Protocol

from runtime.state_transition import TransitionRequest, TransitionResult, validate_transition, verify_consistency


class PersistenceAdapter(Protocol):
    def append_event(self, event: dict) -> None: ...
    def write_state(self, state: dict) -> None: ...
    def read_latest_event(self, entity_id: str) -> dict: ...
    def read_state(self, entity_id: str) -> dict: ...


@dataclass
class TransitionExecutor:
    adapter: PersistenceAdapter
    max_state_write_attempts: int = 3

    def execute(self, current_state: dict, request: TransitionRequest, event_id: str) -> TransitionResult:
        validation = validate_transition(current_state["current_state"], request)
        if validation.status == "REJECTED":
            return validation

        event = {
            "schema_version": "1.0",
            "event_id": event_id,
            "event_type": request.event_type,
            "occurred_at": request.occurred_at,
            "actor_id": request.actor_id,
            "project_id": request.project_id,
            "entity_id": request.entity_id,
            "previous_state": request.expected_previous_state,
            "new_state": request.requested_new_state,
            "correlation_id": request.correlation_id,
            "reason": request.reason,
        }

        next_state = deepcopy(current_state)
        next_state["current_state"] = request.requested_new_state
        next_state["updated_at"] = request.occurred_at
        next_state["updated_by"] = request.actor_id
        next_state["source_event_id"] = event_id

        try:
            self.adapter.append_event(event)
        except Exception:
            return TransitionResult("PERSISTENCE_FAILED", "Event persistence failed before state update.")

        for _ in range(self.max_state_write_attempts):
            try:
                self.adapter.write_state(next_state)
            except Exception:
                continue

            persisted_event = self.adapter.read_latest_event(request.entity_id)
            persisted_state = self.adapter.read_state(request.entity_id)
            verification = verify_consistency(
                persisted_event["new_state"],
                persisted_state["current_state"],
                persisted_event["event_id"],
                persisted_state["source_event_id"],
            )
            if verification.status == "COMMITTED":
                return verification

        return TransitionResult(
            "RECOVERY_REQUIRED",
            "Event was persisted but current state could not be reconciled automatically.",
        )
