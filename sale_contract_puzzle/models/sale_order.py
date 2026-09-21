# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import models

from odoo.addons.fs_file.fields import FSFile

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    file_contract_id = FSFile(string="Contract File")
