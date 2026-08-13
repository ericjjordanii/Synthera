# Synthera Agent Deployment Model

Status: Draft
Schema version: 1.0

A deployment binds a canonical Synthera agent specification to a specific AI provider or runtime.

Deployment rules:
- preserve the canonical agent mission and boundaries
- map abstract capabilities to provider-specific adapters
- declare provider limitations explicitly
- never weaken approval gates silently
- record deployment version separately from agent specification version
- run regression tests before production use
- allow replacement without changing project knowledge or canonical state

ChatGPT is one current deployment target, not the owner of Synthera agents.
