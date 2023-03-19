# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'Student Class'

    name = fields.Char(string="Name", required=True)
    teacher_ids = fields.One2many('teacher.teacher', 'class_id', string="Teachers")

