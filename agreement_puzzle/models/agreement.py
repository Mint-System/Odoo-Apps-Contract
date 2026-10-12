# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import models

_logger = logging.getLogger(__name__)


class Agreement(models.Model):
    # _name = "agreement"
    # _inherit = ["agreement"]
    _inherit = "agreement"
