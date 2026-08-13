# Synthera Production Pipeline for SYN-P001

Trigger: Command Center receives proficiency PASS.

Flow:
1. Unlock production.
2. Send approved lesson package to Content Studio and Proof of Work.
3. Content Studio builds required social assets and posting copy.
4. Proof of Work builds the required technical documentation and evidence package.
5. Store content assets in the configured Drive location.
6. Store technical artifacts in the configured GitHub location.
7. Update canonical operational state and tracker.
8. Return both handoffs to Command Center.
9. Command Center verifies required outputs.
10. Mark Production Complete only when all lesson-type requirements are satisfied.
11. Publishing is a separate state and may occur after Production Complete.

Failure behavior:
- Missing input: stop the affected branch and report blocker.
- Missing evidence: do not substitute generated evidence.
- Integration failure: preserve completed work, report failed destination, and keep state incomplete.
- Conflicting state: canonical operational state wins; flag discrepancy for correction.
