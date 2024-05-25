{
    "name": "Unittest xUnit reports",
    "version": "17.0.0.0.0",
    "depends": ["base",],
    "author": "martin.deconinck@smile.fr",
    "license": "AGPL-3",
    "description": "This module override Odoo testing method to run them with xmlrunner tool.",
    "summary": "",
    "website": "https://smile.eu/fr",
    "category": "Tools",
    "sequence": 20,
    "auto_install": True,
    "installable": True,
    "application": False,
    'external_dependencies': {
        'python': ['unittest-xml-reporting'],
    },
}
