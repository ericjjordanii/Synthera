from runtime.mission_orchestrator import asset_plan, next_after_assessment, production_ready


def test_mission_flow():
    assert next_after_assessment("PASS") == "PROFICIENCY_PASSED"
    assert next_after_assessment("FAIL") == "LEARNING"
    assert asset_plan({"carousel": "VALID", "reel": "MISSING"}) == {"carousel": "ADOPT", "reel": "CREATE"}
    assert production_ready("PASS", {"carousel": "VALID", "lab": "NOT_REQUIRED"})
    assert not production_ready("PASS", {"reel": "MISSING"})
