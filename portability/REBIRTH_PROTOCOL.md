# Synthera Rebirth Protocol

Purpose: restore Synthera on a replacement AI platform without changing project knowledge or system rules.

Minimum restoration sequence:
1. Restore Synthera repository and project repositories.
2. Load the system manifest and project manifests.
3. Load agent specifications, workflows, schemas, and policies.
4. Connect required capability adapters.
5. Restore canonical state and event history.
6. Run migration and regression tests.
7. Verify read/write permissions.
8. Resume from the latest valid project state.

A restoration is not successful until required tests pass.
