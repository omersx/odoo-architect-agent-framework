from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    delivery_urgency = fields.Selection(
        related="sale_id.delivery_urgency",
        string="Delivery Urgency",
        store=True,
        readonly=True,
    )
