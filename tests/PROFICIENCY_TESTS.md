# Synthera Proficiency Regression Tests

Version: 1.0

These tests protect the learning gate from behavioral drift across models, agents, and future AI providers.

## Test 001: Quiz score is not enough
Given a concept lesson with score 100 percent and EXPLAINED not achieved,
Expected: proficiency_gate = FAIL.

## Test 002: Concept lesson passes correctly
Given a concept lesson with score at or above 80 percent and both ASSESSED and EXPLAINED achieved,
Expected: proficiency_gate = PASS.

## Test 003: Lab requires application
Given a lab lesson with ASSESSED and EXPLAINED achieved but no APPLIED evidence,
Expected: proficiency_gate = FAIL.

## Test 004: Troubleshooting requires diagnosis
Given a troubleshooting lesson with successful deployment evidence but no demonstrated diagnostic reasoning or TROUBLESHOT state,
Expected: proficiency_gate = FAIL.

## Test 005: Failed assessment triggers remediation
Given a required assessment component is failed,
Expected: Consultant identifies the weak area, reteaches it, and reassesses with a materially different question or scenario.

## Test 006: Answers are not leaked
Given an active assessment question has been presented and Eric has not answered,
Expected: Consultant does not reveal the solution unless Eric ends the assessment or explicitly requests teaching instead of assessment.

## Test 007: AI-generated artifact is not Eric evidence
Given an agent generated Terraform, commands, screenshots, or documentation but Eric did not execute or validate the claimed technical work,
Expected: APPLIED and TROUBLESHOT remain unachieved.

## Test 008: Command Center gate
Given proficiency_gate = FAIL,
Expected: Command Center does not unlock downstream production.

## Test 009: Mastery cannot be instant
Given a first exposure lesson has passed all immediate lesson requirements,
Expected: MASTERED is not assigned solely from that session.

## Test 010: Stale knowledge requires revalidation
Given a knowledge object is marked STALE or REASSESSMENT_REQUIRED,
Expected: Synthera does not represent it as current mastery until the required revalidation is completed.
