# Synthera Canonical State Model

Status: Draft for feature/state-engine
Schema version: 1.0

## Purpose
Synthera must have one canonical machine-readable representation of current operational truth. Human dashboards, agent conversations, Google Sheets, Drive folders, and project reports are views or consumers of that state, not competing sources of truth.

## Ownership
- Eric is root authority.
- Synthera Core owns the state model and transition rules.
- Project Command Centers may request and apply valid project-scoped state transitions.
- Specialist agents may propose state changes but do not independently redefine canonical state.

## Core state domains
1. Project state
2. Program state
3. Lesson state
4. Knowledge-object state
5. Assessment state
6. Production state
7. Publishing state
8. Artifact state
9. Integration state

## Required properties
Every state record must include:
- schema_version
- entity_id
- entity_type
- project_id when project-scoped
- current_state
- updated_at
- updated_by
- source_event_id

## EJJoftheCloud lesson lifecycle
PLANNED -> READY_TO_LEARN -> LEARNING -> ASSESSMENT_REQUIRED -> PROFICIENCY_PASSED -> PRODUCTION_UNLOCKED -> PRODUCTION_IN_PROGRESS -> PRODUCTION_COMPLETE -> PUBLISHED

Additional states may include BLOCKED, STALE, REASSESSMENT_REQUIRED, and ARCHIVED where applicable.

## Rules
- A state transition must be produced by an event.
- Invalid transitions are rejected rather than silently coerced.
- Current state is derived from accepted events and may not contradict event history.
- Production cannot unlock without a passing proficiency event.
- Published cannot be set unless required publication evidence exists.
- Historical states are never overwritten; current state may change only through a new event.

## Source-of-truth rule
The canonical operational registry is authoritative for current status. GitHub stores the versioned schemas, rules, and portable snapshots. Google Sheets is a human-readable dashboard and must never become an independent authority.
