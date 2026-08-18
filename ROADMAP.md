# Roadmap

## Phase 1: Useful Starter

- Create the core Odoo Architect agent rules.
- Provide a pasteable system prompt.
- Provide repeatable workflows and checklists.
- Implement `biz_bridge_pro` as the reference addon.
- Add industry playbooks for the first five spokes.
- Add static production validator and CI entrypoint.
- Add live Odoo Docker smoke-test workflow.
- Add first product CLI with `info`, `doctor`, `validate`, `scaffold`, `review`, and `smoke-test`.

## Phase 2: Reliable Delivery Kit

- Expand tested addon generators with model, view, security, controller, report, and OWL scaffolds.
- Add more complete module templates.
- Add migration and upgrade checklists.
- Add OWL component templates for POS and website work.
- Add report templates for QWeb PDF documents.
- Add Odoo 18/19 install and update validation results to release notes.
- Add first complete production-grade industry spoke.
- Add eval datasets for generated addon quality.

## Phase 3: Industry Packs

- Build installable extension modules for construction, pharmacy, ecommerce, retail, and consultancy.
- Add functional requirements templates per industry.
- Add demo data and acceptance tests per pack.

## Phase 4: Full Agent Handbook

- Expand role skills.
- Add advanced accounting, inventory, MRP, HR, portal, and integration patterns.
- Add security audit and performance audit workflows.
- Add release packaging and deployment guides.

## Production Gate Before Public Release

- Static validation passes in CI.
- `biz_bridge_pro` installs on Odoo 18 and Odoo 19.
- `biz_bridge_pro` updates cleanly after installation.
- Odoo test suite for `biz_bridge_pro` passes.
- At least one industry spoke passes the same gates.
- Tool adapters are smoke-tested in Codex, Claude Code, Antigravity, and OpenCode/Copencode-style tools.
- CLI unit tests pass.
