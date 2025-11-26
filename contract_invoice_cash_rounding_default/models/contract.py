import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ContractContract(models.Model):
    _inherit = "contract.contract"


    def _recurring_create_invoice(self, date_ref=False):
        moves = super()._recurring_create_invoice(date_ref=date_ref)
        company = self.env.company
        if company.invoice_cash_rounding_id:
            moves.update({"invoice_cash_rounding_id": company.invoice_cash_rounding_id})
        return moves
