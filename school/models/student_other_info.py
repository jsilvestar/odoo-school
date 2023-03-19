# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentOtherInfo(models.Model):
    _name = 'student.other'
    _description = 'student_other'

    name = fields.Char(string="Name")
    blood_group = fields.Selection([
        ('o', 'O+'),
        ('b', 'B+')],
        string='Blood Group'
    )
