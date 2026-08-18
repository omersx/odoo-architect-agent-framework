# Architecture Rules

Use custom addons as the unit of change.

## Module Boundaries

- Put generic reusable behavior in a hub module such as `biz_bridge_pro`.
- Put industry-specific behavior in extension modules such as `biz_bridge_pharmacy`.
- Do not place customer-specific hardcoding in a reusable industry module.
- Keep integration credentials and environment-specific values out of source code.

## Odoo Customization Strategy

- Extend existing models with `_inherit`.
- Create new models only when the data has its own lifecycle, security, or reporting value.
- Avoid duplicating standard Odoo flows.
- Use hooks such as `_prepare_invoice`, `_prepare_procurement_values`, and action overrides when they are the stable extension point for the target flow.

## Data Flow

Prefer explicit propagation for snapshot data and related fields for synchronized display data.

- Snapshot example: copy sale order urgency to an invoice at invoice creation.
- Synchronized example: show sale order urgency on a picking with a stored related field.
