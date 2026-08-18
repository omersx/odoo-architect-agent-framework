from odoo.exceptions import UserError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestBizBridgePro(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create({"name": "Bridge Test Customer"})
        product_values = {
            "name": "Bridge Test Product",
            "type": "consu",
            "list_price": 100.0,
            "standard_price": 40.0,
        }
        if "is_storable" in cls.env["product.template"]._fields:
            product_values["is_storable"] = True

        product_template = cls.env["product.template"].create(product_values)
        cls.product = product_template.product_variant_id

    def test_prepare_invoice_copies_delivery_urgency(self):
        order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "delivery_urgency": "critical",
            }
        )

        invoice_values = order._prepare_invoice()

        self.assertEqual(invoice_values["delivery_urgency"], "critical")

    def test_stock_check_blocks_shortage(self):
        order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "name": self.product.display_name,
                            "product_id": self.product.id,
                            "product_uom_qty": 1.0,
                            "product_uom": self.product.uom_id.id,
                            "price_unit": 100.0,
                        },
                    )
                ],
            }
        )

        with self.assertRaises(UserError):
            order.action_check_live_stock()

    def test_qualified_opportunity_creates_one_quotation(self):
        self.env["ir.config_parameter"].sudo().set_param(
            "biz_bridge_pro.qualified_stage_name",
            "Qualified",
        )
        stage = self.env["crm.stage"].create({"name": "Qualified"})
        lead = self.env["crm.lead"].create(
            {
                "name": "Bridge Test Opportunity",
                "partner_id": self.partner.id,
                "type": "opportunity",
            }
        )

        lead.write({"stage_id": stage.id})
        lead.write({"stage_id": stage.id})

        orders = self.env["sale.order"].search([("opportunity_id", "=", lead.id)])
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders.partner_id, self.partner)
