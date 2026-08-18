# Agent Instructions

You are working in the Odoo Architect Agent Framework.

Your job is to help produce production-minded Odoo customizations, not isolated snippets. Prefer small, upgrade-safe modules, clear dependencies, ORM-first code, XML inheritance, security review, and tests where the risk justifies them.

## Operating Rules

- Never modify Odoo core.
- Prefer `_inherit` over reimplementation.
- Keep business logic in models.
- Keep controllers thin.
- Use XML inheritance with stable XPath targets.
- Use Odoo ORM before raw SQL.
- Add access rights for every new model.
- Review record rules when data visibility changes.
- Design for multi-company and multi-currency unless the feature is explicitly single-company.
- Preserve existing Odoo behavior unless the requirement clearly changes it.
- Document public behavior enough that another Odoo developer can maintain it.

## Delivery Style

For build requests:

1. Identify affected Odoo apps and dependencies.
2. Name the models, views, security records, data files, reports, controllers, assets, and tests needed.
3. Implement in a custom addon or extension addon.
4. Validate syntax and XML structure when local Odoo is unavailable.
5. Run `python tools/validate_framework.py` when changing framework files or example addons.
6. Call out anything that needs verification in a live Odoo database.

For CLI work:

1. Keep the CLI dependency-light and cross-platform.
2. Add or update unit tests in `tests/unit/`.
3. Run `powershell -ExecutionPolicy Bypass -File scripts\test.ps1` on Windows or `bash scripts/test.sh` on Linux/macOS.
4. Run `python tools/validate_framework.py`.

For review requests, lead with findings and file/line references. Focus on bugs, security issues, upgrade risks, missing dependencies, incorrect inheritance, fragile XPath, and missing tests.

## Production Gate

Do not call an addon production-ready until it has passed:

- Static validation with `python tools/validate_framework.py`.
- Live Odoo install/update testing on the target Odoo version.
- Security review for access rights, record rules, and any `sudo()` usage.
- Functional acceptance for the user-facing workflow.

## Naming

- Core modules use `biz_bridge_[name]`.
- Industry extensions use `biz_bridge_[industry]`.
- Python classes use PascalCase.
- Fields use snake_case.
- External IDs use `module_name.record_purpose`.
