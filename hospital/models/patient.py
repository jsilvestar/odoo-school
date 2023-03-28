from odoo import fields, models


class PatientInfo(models.Model):
    _name = "patient.patient"
    _description = "Patient Profile"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    doctor_id = fields.Many2one('doctor.doctor', string="Doctor")
    medicine_ids = fields.Many2many(
        'medicine.medicine',
        'patient_medicine_rel',
        'patient_id',
        'medicine_id',
        string="Medicine"
    )