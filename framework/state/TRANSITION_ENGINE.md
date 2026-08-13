# Synthera Transactional State Transition Engine

Status: Draft for v1
Schema version: 1.0

## Purpose
A state transition is one logical transaction even when persistence requires multiple provider operations.

## Transaction contract
Every transition must contain:
- transaction_id
- project_id
- entity_id
- correlation_id
- actor_id
- expected_previous_state
- requested_new_state
- event_type
- occurred_at
- reason or evidence reference when required

## Execution sequence
1. Read canonical current state.
2. Verify it matches expected_previous_state.
3. Validate the requested transition against lifecycle rules and approval gates.
4. Construct the event and target state snapshot before writing either record.
5. Append the event.
6. Update the current-state snapshot to reference that event.
7. Re-read event history and current state.
8. Commit only when both records agree.
9. If they disagree, enter automatic reconciliation before any downstream workflow continues.

## Consistency gate
No downstream workflow may execute while the latest accepted state-bearing event and canonical current-state snapshot disagree.

## Recovery ladder
1. Retry the normal state write.
2. Retry a minimal state-only write.
3. Use an alternate supported persistence operation.
4. Re-read and verify after every attempt.
5. If reconciliation still fails, mark the transition RECOVERY_REQUIRED and surface a critical blocker to Eric.

Ordinary recoverable connector failures do not require Eric intervention.

## Idempotency
Repeating a transaction with the same transaction_id must not create a second logical transition. If the event exists but the state snapshot is stale, Synthera reconciles the snapshot instead of appending a duplicate event.

## Authority
Eric remains root authority. Command Centers may execute valid project-scoped transitions. Specialist agents may propose transitions but cannot bypass lifecycle gates.

## Completion criteria
A transition is COMMITTED only when:
- the accepted event exists
- current state references that event
- current state equals the event's new_state
- project/entity/correlation identifiers agree

Otherwise the transition remains PENDING or RECOVERY_REQUIRED.