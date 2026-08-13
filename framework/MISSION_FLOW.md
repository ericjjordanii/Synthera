# Mission Orchestration Flow

A mission run coordinates state, assessment, asset discovery, and production decisions.

Flow:
1. select lesson
2. start learning
3. assess Eric
4. PASS moves the lesson to PROFICIENCY_PASSED; FAIL returns to LEARNING
5. only PROFICIENCY_PASSED may move to PRODUCTION_UNLOCKED
6. inventory existing assets
7. adopt valid assets and create only missing requirements
8. production can complete only when required assets are satisfied
9. publishing remains separate

The orchestration layer plans and validates workflow decisions. Persistence must still use the state transition engine and verified event/state writes.
