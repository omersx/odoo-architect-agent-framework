# Industry Playbook: Construction

Construction work usually needs project delivery, site tracking, analytic accounting, procurement, and job costing.

## Recommended Extension

`biz_bridge_construct`

## Dependencies

- `biz_bridge_pro`
- `project`
- `sale_project`
- Accounting and analytic modules required by the target Odoo version

## Features

- Site location on sale orders.
- Project created or linked from confirmed orders.
- Site location passed to projects and invoices.
- Smart button from sales to analytic costs.
- Cost report grouped by project, site, and customer.

## Risks

- Analytic module names and project-sale behavior can vary by Odoo version and edition.
- Do not duplicate standard sale-to-project behavior.
