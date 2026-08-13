# Synthera Proficiency Model

Version: 1.0

Synthera separates recognition from demonstrated capability. A lesson does not become complete simply because Eric says he understands it or passes a multiple-choice quiz.

## Knowledge States

UNSEEN
LEARNING
UNDERSTOOD
ASSESSED
EXPLAINED
APPLIED
TROUBLESHOT
REINFORCED
MASTERED
STALE
REASSESSMENT_REQUIRED

## State Definitions

- UNSEEN: Topic has not been formally studied.
- LEARNING: Active instruction is in progress.
- UNDERSTOOD: Eric indicates the concept makes sense after instruction.
- ASSESSED: Eric has completed a structured knowledge assessment.
- EXPLAINED: Eric can explain the concept accurately in his own words.
- APPLIED: Eric has used the concept in a real or lab environment.
- TROUBLESHOT: Eric has diagnosed and resolved a relevant failure or scenario.
- REINFORCED: Knowledge has been revisited after the initial learning event.
- MASTERED: Strong repeated evidence exists across explanation, application, and problem-solving.
- STALE: Knowledge may no longer reflect current platform behavior or has not been revisited within its review interval.
- REASSESSMENT_REQUIRED: Synthera requires a new assessment before treating the knowledge as current.

## Minimum Gates by Lesson Type

Concept lesson:
- ASSESSED
- EXPLAINED

Hands-on lab:
- ASSESSED
- EXPLAINED
- APPLIED

Troubleshooting lesson:
- ASSESSED
- EXPLAINED
- APPLIED
- TROUBLESHOT

Architecture lesson:
- ASSESSED
- EXPLAINED
- APPLIED when practical
- Design rationale must be defended

Boss Battle / Capstone:
- Multiple relevant competencies must be demonstrated together
- Evidence must include application and problem-solving

## Core Rule

No agent may mark a state as achieved without evidence appropriate to that state.

AI-generated work is not proof that Eric possesses the corresponding skill. Eric must demonstrate understanding and, where required, personally perform the technical activity.

## Production Gate

Command Center may unlock downstream content and proof production only after the lesson's required proficiency states have been satisfied.

## Mastery Rule

MASTERED is never assigned after one lesson. It requires repeated evidence over time, including reinforcement and meaningful application.
