# Construction Extension Sketch

This folder is a starter sketch for an industry spoke module. It is intentionally not a full installable module yet because analytic and project-sale behavior should be verified against the exact Odoo version and edition used by the client.

## Intended Technical Name

`biz_bridge_construct`

## Intended Dependencies

- `biz_bridge_pro`
- `project`
- `sale_project`
- Accounting and analytic modules required by the target database

## Target Features

- Add `site_location` to sale orders.
- Pass `site_location` to invoices.
- Link confirmed sales to projects through standard Odoo sale/project behavior.
- Add a smart button for analytic costs related to the sale order.

Use `industries/construction.md` and `templates/extension-blueprint.md` before implementing this module.
