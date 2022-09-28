from odoo import  fields, models



class PatientTag(models.Model):
    """
    Manage Patient Tags.
    """
    _name = "patient.tag"
    _description = "Manage Patient Tags"
    name = fields.Char(
        "Name"
    )
    active = fields.Boolean("Active", default=True)
    color_select = fields.Integer("Select Color")
    color_picker = fields.Char("Pick Color")
    patient_ids = fields.Many2many("hospital.patient"  , string = "Patients")
