# Synthera Permission Model

Principle: least privilege.

Each agent receives only the capabilities needed for its role.

Rules:
- Read and write permissions are separate.
- High-impact actions require explicit authorization rules.
- Agents cannot grant themselves new permissions.
- Eric is root authority for permission changes.
- Secrets are never stored in prompts, Markdown, or public repositories.
