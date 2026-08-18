# Integration Guide

The framework is designed to be tool-agnostic.

Core idea:

```text
SYSTEM.md + AGENTS.md + workflows + patterns + checklists = shared Odoo brain
```

Adapters make that brain easy to load in different coding agents:

- Claude Code: `CLAUDE.md`
- Antigravity: `.agents/`
- OpenCode: `AGENTS.md` plus `.opencode/agents/odoo-architect.md`
- Copencode: `COPENCODE.md` plus `.opencode/agents/odoo-architect.md`

## Recommended Rule

Keep business and engineering rules in the shared framework files. Keep vendor-specific files thin.

This prevents drift where Claude, Antigravity, OpenCode, and Codex all start giving different Odoo advice.
