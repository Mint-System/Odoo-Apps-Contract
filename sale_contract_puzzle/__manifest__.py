# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Sale Contract Puzzle",
    "summary": """
        Add fields to sale order contracts.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Repository",
    "development_status": "Production/Stable",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["sale_contract", "fs_folder_webdav", "fs_file"],
    "data": [
        "data/fs_storage.xml",
        "views/sale_order.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
    "demo": ["demo/demo.xml"],
}
