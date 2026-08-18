# OpenCode and Copencode

OpenCode-style tools should read `AGENTS.md` and can use `.opencode/agents/odoo-architect.md` as the specialized agent.

Copencode can use the same adapter unless your installed version expects another custom-instructions file name.

## Usage

Use this prompt when the tool does not automatically discover the adapter:

```text
Read SYSTEM.md and AGENTS.md. Then use .opencode/agents/odoo-architect.md as your role instructions. Follow workflows/create-module.md for implementation and checklists/module-checklist.md before final delivery.
```
