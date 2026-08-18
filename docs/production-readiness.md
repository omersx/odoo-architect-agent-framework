# Production Readiness

The framework should be treated as production-ready only when all gates below pass.

## Current Target State

This repository is being hardened from MVP to release candidate.

Production-ready means:

- The framework files are discoverable by supported coding agents.
- The reference addon passes static validation.
- The reference addon installs in a clean Odoo database.
- The reference addon updates in an existing Odoo database.
- Business-critical behavior has Odoo tests.
- Security and access behavior are reviewed.
- Version-sensitive behavior is documented.

## Gates

### Gate 1: Static Validation

Run:

```powershell
.\scripts\validate.ps1
```

On Linux or macOS:

```bash
bash scripts/validate.sh
```

or:

```bash
make validate
```

This checks:

- Required framework files exist.
- Tool adapters exist.
- Odoo manifests parse.
- Manifest data files exist.
- Python files parse.
- XML files parse.
- New model access rights are present.
- Model import files are complete.
- No generated Python cache files are present.

Passing this gate makes the repository a release candidate, not production-certified.

### Gate 2: Odoo 18 Install Test

Start Docker Desktop first and confirm its Linux engine is running.

Run:

```powershell
.\scripts\odoo-smoke-test.ps1 -OdooVersion 18.0
```

On Linux or macOS:

```bash
bash scripts/odoo-smoke-test.sh 18.0 odoo_architect_test_18
```

or:

```bash
make smoke-test-18
```

This performs install and update runs for `biz_bridge_pro`.

### Gate 3: Odoo 19 Install Test

Start Docker Desktop first and confirm its Linux engine is running.

Run:

```powershell
.\scripts\odoo-smoke-test.ps1 -OdooVersion 19.0
```

On Linux or macOS:

```bash
bash scripts/odoo-smoke-test.sh 19.0 odoo_architect_test_19
```

or:

```bash
make smoke-test-19
```

This performs install and update runs for `biz_bridge_pro`.

### Gate 4: Manual Functional Acceptance

Validate in the browser:

- CRM opportunity with a customer creates a draft quotation when moved to `Qualified`.
- Quotation urgency is visible on the sales form.
- Live stock check shows success or blocks shortages.
- Generated invoice receives the urgency value.
- Related warehouse transfer shows the urgency value.

### Gate 5: Release Review

Use:

- `checklists/module-checklist.md`
- `checklists/security-checklist.md`
- `checklists/review-checklist.md`
- `workflows/release.md`

## Odoo 18/19 Compatibility Notes

- Odoo 18/19 product type behavior uses Goods with `type='consu'` and stock tracking through `is_storable`.
- Older Odoo examples may use `type='product'` for storable products.
- Stock logic should check version-sensitive product fields before assuming one selection value.

## Production Label

Use these labels:

- MVP: docs and examples exist, no automated gates.
- Release candidate: static validation and test scaffolding pass.
- Production-ready: static validation plus Odoo 18/19 install and update smoke tests pass.
- Client-certified: production-ready plus client-specific UAT and security review pass.
