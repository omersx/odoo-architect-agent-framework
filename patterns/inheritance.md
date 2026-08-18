# Pattern: Inheritance

Use `_inherit` when extending existing Odoo models.

```python
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_urgency = fields.Selection(
        selection=[
            ("normal", "Normal"),
            ("high", "High"),
            ("critical", "Critical"),
        ],
        default="normal",
    )
```

Avoid `_name` unless creating a new table or delegated inheritance pattern intentionally.
