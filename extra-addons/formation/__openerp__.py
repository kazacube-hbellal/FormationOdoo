# -*- coding: utf-8 -*-
{
    'name': "formation",

    'summary': """
        Module de formation""",

    'description': """
        Ce module propose de gerer des formations:
		- Cours de formations
		- Sessions de formations
		- Inscription aux formations
    """,

    'author': "Kazacube",
    'website': "https://www.kazacube.com/odoo/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'Views/formation.xml',
        'Views/partner.xml',
        'Views/session_board.xml',
        'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
