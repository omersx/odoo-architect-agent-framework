# Integrated Business Bridge

`biz_bridge_pro` is the reference hub addon for the Odoo Architect Agent Framework.

It connects CRM, Sales, Inventory, and Accounting with a small, upgrade-safe customization.

## Features

- Adds `delivery_urgency` to sale orders.
- Adds a sale order header button to check live stock.
- Copies delivery urgency from sale order to invoice during invoice creation.
- Shows delivery urgency on related stock pickings.
- Creates a draft quotation when a CRM lead moves to the `Qualified` stage and has a customer.

## Dependencies

- `crm`
- `sale_management`
- `sale_crm`
- `stock`
- `account`

`sale_crm` is required because it provides the standard CRM opportunity link on quotations.

## Security

This module does not create new models. Standard access rights for CRM, Sales, Stock, and Accounting still apply. The included access CSV is intentionally empty except for the header.

## Configuration

The CRM stage that triggers quotation creation defaults to `Qualified`.

To change it, set this system parameter:

```text
biz_bridge_pro.qualified_stage_name
```

## Verification

After installation:

1. Create a CRM opportunity with a customer.
2. Move it to the `Qualified` stage.
3. Confirm that a draft quotation is created and linked to the opportunity.
4. Set delivery urgency on the quotation.
5. Use `Check Live Stock`.
6. Create an invoice and confirm the urgency copied to the invoice.
7. Confirm related pickings show the urgency.

Automated Odoo tests are available under `tests/` and run during the Docker smoke test when `--test-enable` is used.
