import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class SaleSubscriptionLine(models.Model):
    _inherit = "sale.subscription.line"

    sequence = fields.Integer(string="Sequence", default=10)

    display_type = fields.Selection(
        selection=[
            ('line_section', "Section"),
            ('line_note', "Note"),
        ],
        default=False)