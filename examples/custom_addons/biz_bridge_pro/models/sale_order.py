from odoo import _, fields, models
from odoo.exceptions import UserError

from .common import DELIVERY_URGENCY_SELECTION


class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_urgency = fields.Selection(
        selection=DELIVERY_URGENCY_SELECTION,
        string="Delivery Urgency",
        default="normal",
        required=True,
        tracking=True,
    )

    def action_check_live_stock(self):
        self.ensure_one()

        shortages = []
        for line in self.order_line.filtered(lambda order_line: order_line.product_id):
            product = line.product_id
            if not self._biz_bridge_should_check_stock(product):
                continue

            available_qty = product.with_context(
                warehouse=self.warehouse_id.id,
                warehouse_id=self.warehouse_id.id,
            ).qty_available
            required_qty = line.product_uom._compute_quantity(
                line.product_uom_qty,
                product.uom_id,
            )

            if available_qty < required_qty:
                shortages.append(
                    _("%(product)s: need %(required).2f, available %(available).2f")
                    % {
                        "product": product.display_name,
                        "required": required_qty,
                        "available": available_qty,
                    }
                )

        if shortages:
            raise UserError(
                _("Some products do not have enough stock:\n%s")
                % "\n".join(shortages)
            )

        return {
            "effect": {
                "fadeout": "slow",
                "message": _("All order lines have enough available stock."),
                "type": "rainbow_man",
            }
        }

    def _biz_bridge_should_check_stock(self, product):
        if product.type == "product":
            return True

        template = product.product_tmpl_id
        if "is_storable" in template._fields:
            return template.is_storable

        return product.type == "consu"

    def _prepare_invoice(self):
        values = super()._prepare_invoice()
        values["delivery_urgency"] = self.delivery_urgency
        return values
