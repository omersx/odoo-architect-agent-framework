from odoo import _, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    def write(self, vals):
        result = super().write(vals)
        if "stage_id" in vals:
            self._create_quotation_when_qualified()
        return result

    def _create_quotation_when_qualified(self):
        SaleOrder = self.env["sale.order"]
        qualified_stage_name = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("biz_bridge_pro.qualified_stage_name", "Qualified")
            .strip()
            .lower()
        )
        for lead in self:
            stage_name = (lead.stage_id.name or "").strip().lower()
            if lead.type != "opportunity" or stage_name != qualified_stage_name:
                continue

            existing_order = SaleOrder.search(
                [("opportunity_id", "=", lead.id)],
                limit=1,
            )
            if existing_order:
                continue

            if not lead.partner_id:
                lead.message_post(
                    body=_(
                        "No quotation was created because this opportunity has no customer."
                    )
                )
                continue

            order = SaleOrder.create(
                {
                    "partner_id": lead.partner_id.id,
                    "opportunity_id": lead.id,
                    "origin": lead.name,
                    "company_id": lead.company_id.id or self.env.company.id,
                }
            )
            lead.message_post(
                body=_("Draft quotation %s was created automatically.") % order.name
            )
