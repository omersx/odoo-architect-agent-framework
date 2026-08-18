# Odoo Architect Rules

Use these rules for all Odoo ERP work in this repository.

Shared source of truth:

- `SYSTEM.md`
- `AGENTS.md`
- `system/`
- `patterns/`
- `checklists/`

## Mandatory Rules

- Never edit Odoo core.
- Create custom addons or extension addons.
- Prefer `_inherit` and XML inheritance.
- Declare dependencies in `__manifest__.py`.
- Use ORM before raw SQL.
- Add `ir.model.access.csv` entries for new models.
- Review record rules for sensitive, portal, public, or multi-company data.
- Keep business logic in models.
- Keep controllers thin.
- Treat OWL, POS, website, and accounting hooks as version-sensitive.
- Run `python tools/validate_framework.py` after framework or example addon changes.
- Do not label work production-ready until live Odoo install/update testing passes.
