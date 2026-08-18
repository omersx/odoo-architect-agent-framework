# Industry Playbook: Retail

Retail work focuses on speed, POS usability, receipts, stock visibility, and simple exception handling.

## Recommended Extension

`biz_bridge_retail`

## Dependencies

- `biz_bridge_pro`
- `point_of_sale`

## Features

- POS button to mark an order urgent.
- Sync urgency to the backend order.
- Print urgent delivery text on receipts.
- Add quick-sale handling for non-barcoded items.

## Risks

- POS offline sync must be tested.
- Receipt and OWL APIs can change between versions.
