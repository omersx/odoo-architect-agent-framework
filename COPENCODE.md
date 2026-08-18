# Copencode Adapter

Use the same integration path as OpenCode-style tools:

- Read `AGENTS.md` first.
- Use `SYSTEM.md` as the Odoo Architect identity and rules.
- Use `.opencode/agents/odoo-architect.md` as the specialized agent profile.
- Use `templates/prompt-pack.md` for step-by-step prompting when the tool does not automatically load workflows.

If Copencode in your environment expects a different config file name, keep this file as the human-readable bridge and copy the agent body from `.opencode/agents/odoo-architect.md` into the tool's custom instructions.
