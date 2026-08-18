# Pattern: Fields

## Related Fields

Use related fields for synchronized display or reporting data.

```python
delivery_urgency = fields.Selection(
    related="sale_id.delivery_urgency",
    store=True,
    readonly=True,
)
```

## Computed Fields

Use computed fields for live calculations.

```python
@api.depends("line_ids.amount")
def _compute_total_amount(self):
    for record in self:
        record.total_amount = sum(record.line_ids.mapped("amount"))
```

Store computed fields only when they need search, grouping, reporting, or performance support.
