# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class Agreement(models.Model):
    _inherit = "agreement"

    description = fields.Html()
    yearly_fix_price = fields.Monetary(currency_field="company_currency_id")
    hourly_rate = fields.Monetary(currency_field="company_currency_id")
    cost_cap = fields.Monetary(currency_field="company_currency_id")
    chances = fields.Text()
    risk = fields.Text()
    user_id = fields.Many2one("res.users", string="Responsible Person")
    termination_date = fields.Date()
    termination_reminder_date = fields.Date()
    type_code = fields.Char(
        related="agreement_type_id.code",
        store=True,
    )
    parent_agreement_id = fields.Many2one(
        "agreement",
        string="Parent Agreement",
    )
    child_agreement_ids = fields.One2many(
        "agreement",
        "parent_agreement_id",
        string="Subagreements",
    )
    child_agreement_count = fields.Integer(
        compute="_compute_child_agreement_count",
    )
    company_currency_id = fields.Many2one(
        "res.currency",
        related="company_id.currency_id",
        string="Company Currency",
    )

    @api.depends("child_agreement_ids")
    def _compute_child_agreement_count(self):
        for rec in self:
            rec.child_agreement_count = len(rec.child_agreement_ids)

    def action_open_child_agreements(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Subagreements",
            "res_model": "agreement",
            "view_mode": "list,form",
            "domain": [("parent_agreement_id", "=", self.id)],
        }
