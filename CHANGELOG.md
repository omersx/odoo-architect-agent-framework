# Changelog

## 0.1.0

- Created the Odoo Architect Agent Framework.
- Added root agent prompt and repo instructions.
- Added workflows, patterns, templates, checklists, and industry playbooks.
- Added `biz_bridge_pro` reference addon.
- Added repo-local Codex skill package.
- Added Claude Code, Antigravity, OpenCode, and Copencode adapter files.
- Added static production validator, PowerShell validation wrapper, GitHub Actions workflow, Docker Compose Odoo smoke-test path, Odoo transaction tests, and production readiness docs.
- Hardened the Odoo smoke-test script so Docker failures fail the command instead of reporting false success.
- Added Odoo 18/19 stockability compatibility for `type='consu'` plus `is_storable`.
- Added a current validation report.
- Added Linux/macOS Bash scripts, Make targets, platform support docs, and cross-platform validator checks.
- Added the first `odoo-architect` CLI package with `info`, `doctor`, `validate`, `scaffold`, `review`, and `smoke-test` commands.
- Added CLI unit tests and CI execution for the tests.
- Fixed PowerShell wrappers so native Python command failures return non-zero exit codes.
