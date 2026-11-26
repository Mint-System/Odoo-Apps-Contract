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


    def _prepare_account_move_line(self):
        self.ensure_one()

        if self.display_type:
            return {
                "display_type": self.display_type,
                "name": self.name,
                "sequence": self.sequence,
            }

        account = (
            self.product_id.property_account_income_id
            or self.product_id.categ_id.property_account_income_categ_id
        )
        return {
            "sequence": self.sequence,
            "product_id": self.product_id.id,
            "name": self.name,
            "quantity": self.product_uom_qty,
            "price_unit": self.price_unit,
            "discount": self.discount,
            "price_subtotal": self.price_subtotal,
            "tax_ids": [(6, 0, self.tax_ids.ids)],
            "product_uom_id": self.product_id.uom_id.id,
            "account_id": account.id,
        }

