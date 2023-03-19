# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'


    name = fields.Char(string="Name")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    age = fields.Integer(string='Age')
    register_no = fields.Integer(string='Register Number')
    student_class_id = fields.Many2one('student.class', string='Class')
    class_teacher_id = fields.Many2one('teacher.teacher', string='Teacher')
    blood_group = fields.Many2one('student.other', string='Blood Group')
    # subject_ids = fields.Many2many(
    #     'subject.subject',
    #     'student_subject_rel',
    #     'student_id',
    #     'subject_id',
    #     string='Subjects'
    # )

    subject_ids = fields.Many2many('subject.subject', string='Subjects')
    teacher_id = fields.Many2one('teacher.teacher', string='Teacher')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')],
        string='Gender'
    )
    blood_group = fields.Selection([
        ('o', 'O+'),
        ('b', 'B+')], default='b',
        string='Blood Group'
    )
    teacher_ids = fields.Many2many('teacher.teacher', domain="[ ('class_id','=', student_class_id)]", string='Teachers')

    @api.onchange('first_name', 'last_name')
    def onchange_name(self):
        if self.first_name or self.last_name:
            self.name = '%s %s' % (self.first_name, self.last_name)
