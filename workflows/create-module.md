# Workflow: Create Module

Use this to create a new Odoo addon.

1. Choose the technical name.
2. Declare dependencies.
3. Create `__manifest__.py`, `__init__.py`, and folders.
4. Add model inheritance files.
5. Add XML views with stable XPath.
6. Add security files for new models.
7. Add reports, controllers, assets, or data only when required.
8. Add tests or a focused test plan.
9. Validate syntax and XML.
10. Document installation and acceptance checks.

## Quality Bar

The module should install cleanly, update cleanly, avoid core edits, and make the business behavior obvious to a future Odoo developer.
