# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class CrmLead(models.Model):
    _inherit = "crm.lead"

    agreement_ids = fields.One2many(
        "agreement",
        "lead_id",
        string="Agreements",
    )
    agreement_count = fields.Integer(
        string="Agreement Count",
        compute="_compute_agreement_count",
    )

    @api.depends("agreement_ids")
    def _compute_agreement_count(self):
        for lead in self:
            lead.agreement_count = len(lead.agreement_ids)

    def action_create_agreement(self):
        self.ensure_one()
        if not self.partner_id:
            raise UserError(_("Please set a customer before creating an agreement."))

        base_code = self.name
        code = base_code
        count = 1
        domain = [
            ("code", "=", code),
            ("commercial_partner_id", "=", self.partner_id.commercial_partner_id.id),
            ("company_id", "=", self.env.company.id),
        ]
        while self.env["agreement"].sudo().search_count(domain):
            count += 1
            code = f"{base_code} / {count}"
            domain[0] = ("code", "=", code)

        agreement = self.env["agreement"].create(
            {
                "name": self.name,
                "code": code,
                "partner_id": self.partner_id.id,
                "lead_id": self.id,
                "user_id": self.user_id.id,
            }
        )
        return {
            "type": "ir.actions.act_window",
            "res_model": "agreement",
            "res_id": agreement.id,
            "view_mode": "form",
            "target": "current",
        }
