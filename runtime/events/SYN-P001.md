# SYN-P001 Event Log

## EVT-SYN-P001-0001
- event_type: mission_selected
- occurred_at: 2026-08-13T14:06:00-05:00
- actor_id: SYN-P001-A001
- project_id: SYN-P001
- entity_id: SYN-P001-L001
- new_state: READY_TO_LEARN
- correlation_id: RUN-SYN-P001-L001-0001
- reason: Initialize the first EJJoftheCloud lesson under Synthera runtime v0.

## EVT-SYN-P001-0002
- event_type: lesson_started
- occurred_at: 2026-08-13T14:14:00-05:00
- actor_id: SYN-P001-A001
- project_id: SYN-P001
- entity_id: SYN-P001-L001
- previous_state: READY_TO_LEARN
- new_state: LEARNING
- correlation_id: RUN-SYN-P001-L001-0001

## EVT-SYN-P001-0003
- event_type: assessment_completed
- occurred_at: 2026-08-13T14:27:00-05:00
- actor_id: SYN-P001-A003
- project_id: SYN-P001
- entity_id: SYN-P001-L001
- result: PASS
- evidence: Eric explained cloud computing in his own words, reasoned through a scaling scenario, and correctly explained that cloud resources still depend on physical provider infrastructure.
- correlation_id: RUN-SYN-P001-L001-0001

## EVT-SYN-P001-0004
- event_type: proficiency_passed
- occurred_at: 2026-08-13T14:27:00-05:00
- actor_id: SYN-P001-A003
- project_id: SYN-P001
- entity_id: SYN-P001-L001
- previous_state: LEARNING
- new_state: PROFICIENCY_PASSED
- correlation_id: RUN-SYN-P001-L001-0001
- reason: Day 001 concept proficiency requirements satisfied.

## EVT-SYN-P001-0005
- event_type: production_unlocked
- occurred_at: 2026-08-13T14:27:00-05:00
- actor_id: SYN-P001-A001
- project_id: SYN-P001
- entity_id: SYN-P001-L001
- previous_state: LOCKED
- new_state: UNLOCKED
- correlation_id: RUN-SYN-P001-L001-0001
- reason: Command Center accepted the Cloud Consultant proficiency PASS.

## EVT-SYN-P001-0006
- event_type: state_snapshot_reconciled
- occurred_at: 2026-08-13T15:10:58-05:00
- actor_id: SYN-P001-A001
- project_id: SYN-P001
- entity_id: SYN-P001-L001
- correlation_id: RUN-SYN-P001-RUNTIME-V1-0001
- reason: Add domain-specific source-event references so canonical state can be reconstructed unambiguously from event history.
