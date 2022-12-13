from odoo import fields, models, api, _
import locale


class ContractLine(models.Model):
    _inherit = 'contract.line'
    
    def _insert_markers(self, first_date_invoiced, last_date_invoiced):
        """Append first and last date."""
        res = super()._insert_markers(first_date_invoiced, last_date_invoiced)

        if first_date_invoiced and last_date_invoiced:
            lang_obj = self.env["res.lang"]
            lang = lang_obj.search([("code", "=", self.contract_id.partner_id.lang)])
            locale.setlocale(locale.LC_TIME, lang + '.utf8')

            date_format = "%B %Y"
            res += "\n"
            res += first_date_invoiced.strftime(date_format) + " - " + last_date_invoiced.strftime(date_format)
            
        return res
    
