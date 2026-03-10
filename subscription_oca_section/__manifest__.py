# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Subscription Oca Section",
    "summary": """
        Add notes and section to subscription line table.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch",
    "category": "Repository",
    "development_status": "Production/Stable",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["subscription_oca"],
    "data": [
       "views/subscription_oca.sale_subscription_form.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
