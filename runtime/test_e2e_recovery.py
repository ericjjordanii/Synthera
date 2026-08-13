from runtime.capability_runtime import CapabilityRegistry
from runtime.e2e_recovery import run_production_recovery


class FakeAdapter:
    def __init__(self, failures=0):
        self.failures = failures
        self.calls = 0

    def invoke(self, operation, payload):
        self.calls += 1
        if self.calls <= self.failures:
            raise RuntimeError("temporary failure")
        return payload


def test_recovery_and_blocking():
    registry = CapabilityRegistry()
    registry.register("DOCUMENT_STORAGE", FakeAdapter(failures=1))
    registry.register("SOURCE_CONTROL", FakeAdapter())
    registry.register("TRACKER", FakeAdapter())
    result = run_production_recovery(registry, "PASS", {"carousel": "VALID", "lab": "NOT_REQUIRED"}, [("DOCUMENT_STORAGE", "store", {}), ("SOURCE_CONTROL", "store", {}), ("TRACKER", "update", {})], retries=2)
    assert result.status == "PRODUCTION_COMPLETE"

    blocked = CapabilityRegistry()
    blocked.register("DOCUMENT_STORAGE", FakeAdapter())
    blocked.register("SOURCE_CONTROL", FakeAdapter(failures=5))
    blocked.register("TRACKER", FakeAdapter())
    result = run_production_recovery(blocked, "PASS", {"carousel": "VALID"}, [("DOCUMENT_STORAGE", "store", {}), ("SOURCE_CONTROL", "store", {}), ("TRACKER", "update", {})], retries=1)
    assert result.status == "BLOCKED"
    assert result.completed_capabilities == ("DOCUMENT_STORAGE",)
    assert result.failed_capability == "SOURCE_CONTROL"
