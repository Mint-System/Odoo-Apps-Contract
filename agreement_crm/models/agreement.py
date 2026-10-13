# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Agreement(models.Model):
    _inherit = "agreement"

    lead_id = fields.Many2one(
        "crm.lead",
        string="Lead",
        ondelete="set null",
    )
    user_id = fields.Many2one(
        "res.users",
        string="Salesperson",
        ondelete="set null",
    )
