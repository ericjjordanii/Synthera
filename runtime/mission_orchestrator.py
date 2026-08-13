from asset_discovery import action_for


def next_after_assessment(proficiency: str) -> str:
    if proficiency == "PASS":
        return "PROFICIENCY_PASSED"
    return "LEARNING"


def next_after_proficiency(state: str) -> str:
    if state != "PROFICIENCY_PASSED":
        raise ValueError("production remains locked before proficiency pass")
    return "PRODUCTION_UNLOCKED"


def asset_plan(statuses: dict[str, str]) -> dict[str, str]:
    return {name: action_for(status) for name, status in statuses.items()}


def production_ready(proficiency: str, statuses: dict[str, str]) -> bool:
    if proficiency != "PASS":
        return False
    blocking = {"PARTIAL", "STALE", "MISSING"}
    return not any(status in blocking for status in statuses.values())
