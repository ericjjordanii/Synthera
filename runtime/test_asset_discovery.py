from asset_discovery import action_for


def test_actions():
    cases = {
        "VALID": "ADOPT",
        "PARTIAL": "COMPLETE",
        "STALE": "REVIEW",
        "MISSING": "CREATE",
        "NOT_REQUIRED": "SKIP",
    }
    for status, expected in cases.items():
        assert action_for(status) == expected
