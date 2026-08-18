# Claude Code Adapter

Use this repository as the Odoo Architect Agent Framework.

Read these shared instructions first:

- @SYSTEM.md
- @AGENTS.md

For Odoo module creation, also read:

- @workflows/analyze-requirements.md
- @workflows/create-module.md
- @checklists/module-checklist.md
- @checklists/security-checklist.md

For extension modules, also read:

- @workflows/extend-module.md
- @templates/extension-blueprint.md
- @patterns/crm-sales-accounting.md

For reviews, also read:

- @workflows/review-module.md
- @checklists/review-checklist.md

## Claude Code Behavior

- Treat `SYSTEM.md` and `AGENTS.md` as the source of truth.
- Do not duplicate standard Odoo behavior unless a requirement explicitly asks for it.
- Implement changes directly when the requirement is clear.
- Keep edits scoped to the relevant addon, template, workflow, or framework file.
- Validate Python syntax and XML structure when a local Odoo database is unavailable.
- Clearly label anything that still needs live Odoo verification.
- Run `python tools/validate_framework.py` after framework or example addon changes.
- Do not call an addon production-ready until target-version Odoo install/update tests pass.
