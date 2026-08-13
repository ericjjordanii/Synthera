# Capability Failure Contract

Integration failures must be explicit and recoverable.

Required behavior:
- preserve successful prior work
- record the failed capability and operation
- emit an integration_failed event
- mark dependent workflow state as BLOCKED when necessary
- never fabricate success
- allow retry after recovery
- emit integration_recovered when service resumes
