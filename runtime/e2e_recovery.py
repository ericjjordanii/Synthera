from dataclasses import dataclass

from runtime.capability_runtime import CapabilityRegistry
from runtime.mission_orchestrator import production_ready


@dataclass(frozen=True)
class RecoveryWorkflowResult:
    status: str
    completed_capabilities: tuple[str, ...]
    failed_capability: str | None = None


def run_production_recovery(
    registry: CapabilityRegistry,
    proficiency: str,
    asset_statuses: dict[str, str],
    operations: list[tuple[str, str, dict]],
    retries: int = 2,
) -> RecoveryWorkflowResult:
    if proficiency != "PASS":
        return RecoveryWorkflowResult("BLOCKED", ())

    completed: list[str] = []
    for capability, operation, payload in operations:
        result = registry.invoke(capability, operation, payload, retries=retries)
        if result.status == "FAILED":
            return RecoveryWorkflowResult("BLOCKED", tuple(completed), capability)
        completed.append(capability)

    if not production_ready(proficiency, asset_statuses):
        return RecoveryWorkflowResult("INCOMPLETE", tuple(completed))

    return RecoveryWorkflowResult("PRODUCTION_COMPLETE", tuple(completed))
