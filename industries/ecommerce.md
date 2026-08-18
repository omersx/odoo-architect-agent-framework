# Industry Playbook: Ecommerce

Ecommerce work connects website checkout, portal visibility, sales, delivery, and invoicing.

## Recommended Extension

`biz_bridge_ecommerce`

## Dependencies

- `biz_bridge_pro`
- `website_sale`

## Features

- Add delivery urgency to checkout.
- Save checkout urgency on the backend sale order.
- Show urgency in customer portal order views.
- Keep website controllers thin and validated.

## Risks

- Website templates and controllers are version-sensitive.
- Never trust website form input without validation.
