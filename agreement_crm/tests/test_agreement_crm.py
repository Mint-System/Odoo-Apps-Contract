# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.exceptions import UserError
from odoo.tests.common import TransactionCase


class TestAgreementCrm(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create({"name": "Test Partner"})
        cls.lead = cls.env["crm.lead"].create(
            {
                "name": "Test Lead",
                "partner_id": cls.partner.id,
            }
        )

    def test_create_agreement_from_lead(self):
        action = self.lead.action_create_agreement()
        agreement = self.env["agreement"].browse(action["res_id"])
        self.assertEqual(agreement.name, self.lead.name)
        self.assertEqual(agreement.partner_id, self.partner)
        self.assertEqual(agreement.lead_id, self.lead)
        self.assertEqual(agreement.user_id, self.lead.user_id)

    def test_create_agreement_without_partner_raises(self):
        lead_no_partner = self.env["crm.lead"].create({"name": "No Partner Lead"})
        with self.assertRaises(UserError):
            lead_no_partner.action_create_agreement()

    def test_agreement_count(self):
        self.assertEqual(self.lead.agreement_count, 0)
        self.lead.action_create_agreement()
        self.assertEqual(self.lead.agreement_count, 1)

    def test_create_multiple_agreements_from_lead(self):
        action1 = self.lead.action_create_agreement()
        agreement1 = self.env["agreement"].browse(action1["res_id"])
        self.assertEqual(agreement1.code, self.lead.name)

        action2 = self.lead.action_create_agreement()
        agreement2 = self.env["agreement"].browse(action2["res_id"])
        self.assertEqual(agreement2.code, f"{self.lead.name} / 2")
