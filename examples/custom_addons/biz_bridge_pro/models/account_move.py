from odoo import fields, models

from .common import DELIVERY_URGENCY_SELECTION


class AccountMove(models.Model):
    _inherit = "account.move"

    delivery_urgency = fields.Selection(
        selection=DELIVERY_URGENCY_SELECTION,
        string="Delivery Urgency",
        copy=False,
        readonly=True,
    )
