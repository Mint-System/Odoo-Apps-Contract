# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Agreement CRM",
    "summary": """
        Create agreements from leads.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Repository",
    "development_status": "Production/Stable",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["agreement", "crm"],
    "data": [
        "views/crm_lead.xml",
        "views/agreement.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
