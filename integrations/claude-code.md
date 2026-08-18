# Claude Code

Claude Code can use `CLAUDE.md` at the repository root.

This project keeps `CLAUDE.md` as a thin adapter that imports or points to:

- `SYSTEM.md`
- `AGENTS.md`
- Relevant workflows and checklists

## Usage

Open this repository in Claude Code and ask for Odoo work normally.

Example:

```text
Use the Odoo Architect framework. Create a biz_bridge_pharmacy extension module that depends on biz_bridge_pro and blocks expired lots during transfer validation.
```

For slash-command style use, see:

```text
.claude/commands/odoo-module.md
```
