from dataclasses import dataclass
from typing import Any, Protocol


class CapabilityAdapter(Protocol):
    def invoke(self, operation: str, payload: dict[str, Any]) -> Any: ...


@dataclass(frozen=True)
class CapabilityResult:
    status: str
    capability: str
    operation: str
    attempts: int
    value: Any = None
    error: str | None = None


class CapabilityRegistry:
    def __init__(self):
        self._adapters: dict[str, CapabilityAdapter] = {}

    def register(self, capability: str, adapter: CapabilityAdapter) -> None:
        self._adapters[capability] = adapter

    def invoke(self, capability: str, operation: str, payload: dict[str, Any], retries: int = 0) -> CapabilityResult:
        adapter = self._adapters.get(capability)
        if adapter is None:
            return CapabilityResult(
                status="FAILED",
                capability=capability,
                operation=operation,
                attempts=0,
                error="No adapter is registered for this capability.",
            )

        attempts = 0
        last_error = None
        while attempts <= retries:
            attempts += 1
            try:
                value = adapter.invoke(operation, payload)
                status = "RECOVERED" if attempts > 1 else "SUCCESS"
                return CapabilityResult(status, capability, operation, attempts, value=value)
            except Exception as exc:
                last_error = str(exc)

        return CapabilityResult(
            status="FAILED",
            capability=capability,
            operation=operation,
            attempts=attempts,
            error=last_error,
        )
