# Pattern: CRM to Sales to Accounting

When a value begins on a sale order and must become part of an invoice, use an invoice preparation hook.

```python
def _prepare_invoice(self):
    values = super()._prepare_invoice()
    values["delivery_urgency"] = self.delivery_urgency
    return values
```

When a sale order needs to link back to a CRM opportunity, depend on the standard CRM/Sales bridge module instead of assuming both apps alone provide the relation.

For `sale.order.opportunity_id`, declare `sale_crm` in the manifest.
