# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging
import os

from slugify import slugify  # pylint: disable=missing-manifest-dependency

from odoo import models

_logger = logging.getLogger(__name__)


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    def _enforce_meaningful_storage_filename(self) -> None:
        our_records = self.filtered(
            lambda a: a.res_model == "sale.order" and a.res_field == "file_contract_id" and a.store_fname
        )
        super(IrAttachment, self - our_records)._enforce_meaningful_storage_filename()

        renamed_attachments = {}
        for attachment in our_records:
            if not self._is_file_from_a_storage(attachment.store_fname):
                continue

            fs, storage, filename = attachment._get_fs_parts()

            if self.env["fs.storage"]._must_use_filename_obfuscation(storage):
                attachment.fs_filename = filename
                continue

            sale_order = self.env["sale.order"].browse(attachment.res_id).exists()
            partner_name = slugify(sale_order.partner_id.name or "Unknown") if sale_order else "Unknown"

            new_filename = attachment._build_fs_filename()
            new_path = os.path.join(partner_name, "Contract", new_filename)

            if filename in renamed_attachments:
                if renamed_attachments[filename] == new_path:
                    continue
                else:
                    fs.copy(renamed_attachments[filename], new_path)
            else:
                parent_dir = os.path.dirname(new_path)
                if not fs.exists(parent_dir):
                    fs.makedirs(parent_dir)
                fs.rename(filename, new_path)

            renamed_attachments[filename] = new_path
            attachment.fs_filename = new_filename
            attachment._force_write_store_fname(f"{storage}://{new_path}")
            self._fs_mark_for_gc(attachment.store_fname)
