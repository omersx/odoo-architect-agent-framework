# Workflow: Release

Before delivery:

1. Install on a clean database.
2. Upgrade the module on an existing database.
3. Test the main business flow.
4. Test normal user permissions.
5. Test manager permissions.
6. Review logs for XML, access, and compute errors.
7. Confirm no demo/test data is loaded in production mode.
8. Prepare release notes and rollback notes.

## Required Commands

Run static validation:

```powershell
.\scripts\validate.ps1
```

Run live install tests:

```powershell
.\scripts\odoo-smoke-test.ps1 -OdooVersion 18.0
.\scripts\odoo-smoke-test.ps1 -OdooVersion 19.0 -Database odoo_architect_test_19
```

Document results in `docs/release-template.md`.
