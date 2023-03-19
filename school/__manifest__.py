# -*- coding: utf-8 -*-
{
    'name': "School",
    'author': "Reena Silvestar",
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
         'views/student_views.xml',
         'views/student_class_views.xml',
         'views/teacher_views.xml',
         'views/subject_views.xml',
         'views/student_other_info_views.xml',
         'views/school_menu_items.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
