from odoo import fields, models


class DoctorInfo(models.Model):
    _name = "doctor.doctor"
    _description = "Doctor Profile"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    date_of_birth = fields.Date(string="Date of Birth")
    phone = fields.Char(string="Phone")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')],
        'Gender'
    )
    status = fields.Selection([
        ('active', 'Active'),
        ('in_active', 'In-Active')],
        'Status',
        default='active')
    profession = fields.Selection(
        [('doctor', 'Doctor'),
         ('nurse', 'Nurse')],
        'Profession',
        default='doctor'
    )
    doctor_qualification = fields.Char(string="Doctor Qualification")
    nurse_qualification = fields.Char(string="Nurse Qualification")
    patient_ids = fields.One2many('patient.details',  'doctor_id', string="Doctor")


class PatientDetails(models.Model):
    _name = "patient.details"

    patient_id = fields.Many2one('patient.patient', string='Patient')
    fees = fields.Float(string="Fees")
    doctor_id = fields.Many2one('doctor.doctor', string="Doctor")
    medicine_ids = fields.Many2many('medicine.medicine', string="Medicine")