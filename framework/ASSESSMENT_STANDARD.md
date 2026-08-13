# Synthera Assessment Standard

Version: 1.0

The assessment system exists to verify that Eric understands the lesson before downstream automation begins.

## Required Assessment Components

Every concept lesson assessment must include:
1. Recall questions
2. Conceptual reasoning questions
3. Explain-it-back prompt
4. At least one scenario question when the topic supports scenarios

Hands-on lessons must additionally include:
5. Application validation
6. Evidence from Eric's own execution when the skill claim depends on execution

Troubleshooting lessons must additionally include:
7. Diagnostic reasoning
8. Root-cause explanation
9. Fix validation

## Scoring

Default written/quiz threshold: 80 percent.

A score of 80 percent or higher does not by itself grant proficiency. The explain-it-back requirement and all lesson-type gates must also pass.

## Explain-It-Back Rule

Eric must explain the core concept in his own words without simply reproducing the lesson wording. The Cloud Consultant evaluates whether the explanation demonstrates accurate mental models and catches material misconceptions.

## Scenario Rule

Scenario questions should test transfer, not memorization. They should ask Eric to choose, diagnose, predict, compare, or justify a technical decision.

## Remediation Loop

If any required component fails:
1. Identify the exact weak area.
2. Reteach only the weak area unless broader misunderstanding is evident.
3. Ask Eric to restate the corrected concept.
4. Generate a new reassessment using different wording or scenarios.
5. Repeat until all required gates pass or Eric ends the session.

## Anti-Gaming Rule

Do not reveal answers before Eric commits to a response when the interaction is being used as an assessment.

## Human Ownership Rule

The system may generate questions, grade responses, and recommend proficiency. It may not fabricate lab execution, validation evidence, or technical actions that Eric did not personally perform.

## Handoff Result

The Cloud Consultant returns a structured result to Command Center containing:
- lesson_id
- assessment_attempts
- score
- states_achieved
- weak_areas
- remediation_completed
- required_states_satisfied
- proficiency_gate: PASS or FAIL
