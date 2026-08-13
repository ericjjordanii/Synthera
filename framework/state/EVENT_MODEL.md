# Synthera Event Model

Status: Draft for feature/state-engine
Schema version: 1.0

## Principle
Synthera preserves meaningful history as append-only events. Events explain how current state was reached.

## Event requirements
Every accepted event must include:
- schema_version
- event_id
- event_type
- occurred_at
- actor_id
- project_id when applicable
- entity_id
- previous_state when applicable
- new_state when applicable
- reason or evidence reference when required
- correlation_id for one workflow run

## Event categories
- mission_selected
- lesson_started
- assessment_completed
- remediation_started
- proficiency_passed
- proficiency_failed
- production_unlocked
- production_started
- artifact_created
- artifact_verified
- production_completed
- published
- knowledge_marked_stale
- reassessment_completed
- integration_failed
- integration_recovered
- manual_override

## Append-only rule
Accepted historical events are not edited or deleted to make the record look cleaner. Corrections are represented by new corrective events.

## Manual overrides
Eric may authorize a manual override. An override must preserve:
- who authorized it
- why
- the prior state
- the resulting state
- timestamp

## Correlation
All events produced during one end-to-end mission run share a correlation_id so Synthera can reconstruct the full workflow later.

## Relationship to state
The event log is historical evidence. The canonical state registry stores the latest accepted state for efficient access. If they disagree, the inconsistency is a system defect and must be reconciled from the event history.
