# Odoo Architect CLI

The `odoo-architect` CLI is the product layer for this framework.

It turns the handbook, skills, templates, validators, and Docker smoke tests into repeatable commands.

## Install From This Repository

From the repository root:

```bash
python -m pip install -e .
```

Then run:

```bash
odoo-architect info
```

## Commands

### `info`

Show CLI version, framework root, Python version, platform, and command list.

```bash
odoo-architect info
```

### `doctor`

Check framework files and local tool availability.

```bash
odoo-architect doctor
odoo-architect doctor --strict
```

### `validate`

Run the production static validator.

```bash
odoo-architect validate
```

### `scaffold`

Create a minimal installable Odoo addon skeleton.

```bash
odoo-architect scaffold biz_bridge_pharmacy \
  --extension \
  --depends stock,product_expiry,point_of_sale \
  --summary "Pharmacy extension for biz_bridge_pro."
```

By default, addons are created under:

```text
examples/custom_addons
```

### `review`

Run a lightweight static review on one addon.

```bash
odoo-architect review examples/custom_addons/biz_bridge_pro
```

### `smoke-test`

Run live Odoo install and update smoke tests through Docker Compose.

```bash
odoo-architect smoke-test --odoo-version 18.0 --database odoo_architect_test_18
odoo-architect smoke-test --odoo-version 19.0 --database odoo_architect_test_19
```

## Design Notes

This CLI is intentionally local-first:

- No cloud dependency.
- No third-party Python runtime dependencies.
- Works from source or editable install.
- Uses the same production gate as `tools/validate_framework.py`.
- Uses Docker Compose only for live Odoo validation.
