---
name: odoo-architect
description: Design, implement, review, and document Odoo custom addons using upgrade-safe architecture, ORM, XML, security, testing, and industry extension patterns.
metadata:
  short-description: Build and review Odoo addons
---

# Odoo Architect

Use this skill when the task involves Odoo ERP modules, custom addons, XML views, ORM logic, OWL/POS/website customization, security, migration, or review.

The goal is production-minded Odoo work: clear business analysis, correct dependencies, upgrade-safe inheritance, secure data access, and maintainable implementation.

## Default Behavior

- Treat Odoo custom addons as the normal delivery unit.
- Never modify Odoo core.
- Prefer `_inherit`, stable hooks, and XML inheritance.
- Declare all required dependencies in `__manifest__.py`.
- Add access rights for every new model.
- Review record rules when the data is sensitive or crosses companies/users.
- Use related stored fields for synchronized reportable values.
- Use computed fields for live calculations.
- Keep controllers thin and validate public input.
- Call out version-sensitive areas before claiming a change is final.

## Task Routing

- For new module work, read `references/module-workflow.md`.
- For review work, read `references/review-gates.md`.
- For industry extension work, read `references/industry-routing.md`.
- For security-sensitive work, read `references/security-gates.md`.

Read only the references relevant to the current task.

## Hub and Spoke Pattern

Use `biz_bridge_pro` as the generic hub and `biz_bridge_[industry]` as extension spokes.

Hub logic should be reusable across industries. Spoke logic should depend on the hub and add only industry-specific behavior.
