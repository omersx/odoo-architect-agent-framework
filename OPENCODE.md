# OpenCode Adapter

OpenCode-style agents should use:

- `AGENTS.md` for repository-level instructions.
- `.opencode/agents/odoo-architect.md` for the Odoo-specific agent profile.
- `SYSTEM.md` as the shared role and rules prompt.

When creating or reviewing Odoo modules, load the relevant workflow from `workflows/` and the relevant checklist from `checklists/`.

If your OpenCode build supports custom agent frontmatter, keep the body of `.opencode/agents/odoo-architect.md` as the instruction text and adapt only the metadata keys required by your version.
