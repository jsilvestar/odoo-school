# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subject(models.Model):
    _name = 'subject.subject'
    _description = 'Subject'

    name = fields.Char(string="Name")
