# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    parent_contract_id = fields.Many2one(
        comodel_name="sale.order",
        string="Parent Contract",
    )
    child_contract_ids = fields.One2many(
        comodel_name="sale.order",
        inverse_name="parent_contract_id",
        string="Child Contracts",
    )
    child_contract_count = fields.Integer(
        compute="_compute_child_contract_count",
    )

    def _compute_child_contract_count(self):
        for order in self:
            order.child_contract_count = len(order.child_contract_ids)

    def action_view_child_contracts(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Child Contracts",
            "res_model": "sale.order",
            "view_mode": "tree,form",
            "domain": [("parent_contract_id", "=", self.id)],
            "context": {"default_parent_contract_id": self.id},
        }
