# Odoo Version Policy

Target Odoo 18 first and keep Odoo 19 compatibility in mind.

## Version-Sensitive Areas

Verify against the target Odoo database before release when touching:

- OWL components and asset bundles.
- Website controllers.
- POS models and receipt rendering.
- Accounting hooks.
- View IDs and XPath targets.
- Module names around analytic accounting, project sales, and CRM/Sales integration.
- Product stockability fields. Odoo 18/19 use Goods plus `is_storable`; older patterns often use `type='product'`.

## Compatibility Rule

When a feature depends on a bridge module, declare that bridge dependency directly. For example, CRM quotation linkage should depend on `sale_crm`, not only on `crm` and `sale_management`.
