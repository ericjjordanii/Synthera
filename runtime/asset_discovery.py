ACTIONS = {
    "VALID": "ADOPT",
    "PARTIAL": "COMPLETE",
    "STALE": "REVIEW",
    "MISSING": "CREATE",
    "NOT_REQUIRED": "SKIP",
}


def action_for(status: str) -> str:
    return ACTIONS[status]
