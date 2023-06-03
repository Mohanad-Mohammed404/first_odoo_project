{
    'name': "University System",
    'summary': """University Odoo task""",
    'description': """Student can add his data here to make him, so that he can join the college he wants""",
    'author': "Mohannad Mohammed",
    'website': "https://www.linkedin.com/in/mohannad404/",
    'category': 'Registration',
    'version': '1.0',
    'sequence': 1,
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/students.xml',
        'views/faculty_desire.xml',
        'views/menus.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install' : False,
    'license': 'LGPL-3',
}
# -*- coding: utf-8 -*-


