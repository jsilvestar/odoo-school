# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'teacher.teacher'
    _description = 'teacher'

    name = fields.Char(string="Name")
    age = fields.Integer(string='Age')
    student_ids = fields.One2many('student.student', 'teacher_id', string="Students")
    class_id = fields.Many2one('student.class', string="Class")
    teacher_id = fields.Many2one('teacher.teacher', string='Teacher')
    student_id = fields.Many2one('student.student', string='Student')
