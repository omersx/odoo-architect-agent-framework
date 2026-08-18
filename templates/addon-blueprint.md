# Template: Odoo Addon Blueprint

```text
custom_addons/
  my_module/
    __init__.py
    __manifest__.py
    models/
      __init__.py
      sale_order.py
    views/
      sale_order_views.xml
    security/
      ir.model.access.csv
    tests/
      __init__.py
      test_main_flow.py
```

## Manifest Checklist

- `name`
- `version`
- `summary`
- `depends`
- `data`
- `license`
- `installable`
- `application`

## Prompt

Create a custom Odoo addon named `[technical_name]`.

Business goal:

`[describe the workflow]`

Rules:

- Do not edit Odoo core.
- Use `_inherit` for existing models.
- Declare all dependencies.
- Use XML XPath for views.
- Add access rights for new models.
- Add tests or a test plan.
