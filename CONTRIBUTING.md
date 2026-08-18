# Contributing

Thank you for helping improve the Odoo Architect Agent Framework.

This project is for production-minded Odoo custom addon development, agent workflows, CLI tooling, templates, and validation gates.

## Good Contributions

- Odoo addon patterns that are upgrade-safe.
- CLI improvements with tests.
- Better validators and release gates.
- New industry playbooks.
- Odoo 18/19 compatibility fixes.
- Clear documentation and examples.

## Before Opening a Pull Request

Run:

```bash
python tools/validate_framework.py
```

Run CLI tests:

```bash
python -B -m unittest discover -s tests/unit -p "test_*.py"
```

On Windows, you can use:

```powershell
.\scripts\test.ps1
.\scripts\validate.ps1
```

## Development Rules

- Never modify Odoo core.
- Prefer `_inherit`, ORM, and XML inheritance.
- Add access rights for every new model.
- Keep the CLI dependency-light and cross-platform.
- Add tests for CLI behavior.
- Document anything that requires live Odoo validation.
