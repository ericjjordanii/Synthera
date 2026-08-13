from runtime.capability_runtime import CapabilityRegistry


class FakeAdapter:
    def __init__(self, failures=0):
        self.failures = failures
        self.calls = 0

    def invoke(self, operation, payload):
        self.calls += 1
        if self.calls <= self.failures:
            raise RuntimeError("temporary provider failure")
        return {"operation": operation, "payload": payload}


def test_successful_capability_call():
    registry = CapabilityRegistry()
    registry.register("SOURCE_CONTROL", FakeAdapter())
    result = registry.invoke("SOURCE_CONTROL", "read", {"path": "README.md"})
    assert result.status == "SUCCESS"
    assert result.attempts == 1


def test_retry_recovers_provider_failure():
    registry = CapabilityRegistry()
    adapter = FakeAdapter(failures=1)
    registry.register("DOCUMENT_STORAGE", adapter)
    result = registry.invoke("DOCUMENT_STORAGE", "list", {"folder": "SYN-P001"}, retries=2)
    assert result.status == "RECOVERED"
    assert result.attempts == 2
    assert adapter.calls == 2


def test_exhausted_retries_are_explicit_failure():
    registry = CapabilityRegistry()
    registry.register("TRACKER", FakeAdapter(failures=5))
    result = registry.invoke("TRACKER", "update", {"lesson": "L002"}, retries=1)
    assert result.status == "FAILED"
    assert result.attempts == 2
    assert result.error == "temporary provider failure"


def test_missing_adapter_never_fabricates_success():
    result = CapabilityRegistry().invoke("EMAIL", "send", {})
    assert result.status == "FAILED"
    assert result.attempts == 0
