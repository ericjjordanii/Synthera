# ADR-0001: Runtime State Backend v0

Status: Accepted for v0.x

## Context
Synthera needs a canonical operational registry before a dedicated database is deployed.

## Decision
Use versioned machine-readable files in the Synthera GitHub repository as the temporary v0 operational state backend.

## Constraints
- GitHub is temporary runtime storage, not the long-term target.
- Every accepted state change must preserve event history.
- Google Sheets remains a dashboard only.
- Chat history is never authoritative.
- Secrets and sensitive credentials are excluded.

## Future migration
Move operational state to a dedicated database when Synthera requires higher write frequency, concurrency, richer querying, or application-scale automation. The migration must preserve entity IDs, event history, schema versions, and current state.

## Consequence
Synthera can operate now without prematurely introducing Azure database infrastructure while retaining a documented migration path.
