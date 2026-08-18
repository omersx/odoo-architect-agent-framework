# Template: Industry Extension Blueprint

Technical name: `biz_bridge_[industry]`

Dependency rule:

```python
'depends': ['biz_bridge_pro', '[required_odoo_apps]']
```

## Extension Prompt

Create an Odoo extension module named `biz_bridge_[industry]`.

It depends on `biz_bridge_pro` and must reuse hub behavior instead of duplicating it.

Industry:

`[industry name]`

Features:

1. `[feature one]`
2. `[feature two]`
3. `[feature three]`

Deliver:

- Manifest.
- Models.
- Views.
- Security.
- Tests or test plan.
- Install and acceptance steps.
