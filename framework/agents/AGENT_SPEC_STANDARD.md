# Synthera Agent Specification Standard

Status: Draft
Schema version: 1.0

Every Synthera agent is defined independently of any AI provider.

Required agent properties:
- agent_id
- name
- project_id
- mission
- responsibilities
- prohibited_actions
- inputs
- outputs
- capabilities
- permissions
- handoff_rules
- failure_behavior
- approval_gates
- test_requirements
- specification_version

The canonical agent specification lives in Synthera. Provider-specific deployments are derived implementations and must not become the source of truth.
