# Synthera Migration Standard

Migrations must preserve behavior, state, history, and project ownership.

Rules:
- schemas are versioned
- migrations are reversible when practical
- old records are preserved until conversion is verified
- provider changes use adapters rather than rewriting agent missions
- migration completion requires regression tests
- Eric authorizes destructive migration steps
