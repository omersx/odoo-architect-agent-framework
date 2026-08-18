# Industry Playbook: Pharmacy

Pharmacy work needs traceability, expiry control, controlled product handling, patient references, and POS receipt customization.

## Recommended Extension

`biz_bridge_pharmacy`

## Dependencies

- `biz_bridge_pro`
- `stock`
- `product_expiry`
- `point_of_sale`

## Features

- Block expired lots during transfer validation.
- Show batch and expiry on relevant documents.
- Add doctor and patient references.
- Print required references on POS receipts.
- Keep audit trail for controlled products.

## Risks

- Medical data can be sensitive.
- POS customizations are version-sensitive.
- Record rules must be reviewed carefully.
