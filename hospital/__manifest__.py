# -*- coding: utf-8 -*-
{
    'name': "Hospital",
    'author': "ABC",
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/medicine_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
