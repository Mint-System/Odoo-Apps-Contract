# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class AgreementType(models.Model):
    _inherit = "agreement.type"

    name = fields.Char(translate=True)
    code = fields.Char()
