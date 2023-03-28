from odoo import fields, models


class Medicine(models.Model):
    _name = "medicine.medicine"
    _description = "Medicine Details"

    name = fields.Char('Name')
