from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    """
    Manage Hospital Patients.
    """
    _name = "hospital.patient"
    _description = "Managing Hospital Patients."
    _inherit = ["mail.thread", "mail.activity.mixin"]
    # _rec_name = "name"

    # String fields:
    birth = fields.Date("Date Of Birth")
    name = fields.Char(
        "Name"
    )
    age = fields.Integer("Age", tracking=True, compute="_compute_age")
    active = fields.Boolean("Active", default=True)
    image = fields.Image("Image")
    tag_ids = fields.Many2many("patient.tag", string="Tags")
    gender = fields.Selection(
        [("male", "Male"),
         ("female", "Female")
         ],
        "Gender",
    )
    ref = fields.Char(
        "Reference", tracking=True
    )

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth:
                rec.age = today.year - rec.birth.year
            else:
                rec.age = 1

    @api.model
    def create(self, vals):
        vals["ref"] = self.env["ir.sequence"].next_by_code("hospital.patient")
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        # if not self.ref and not vals.get("ref"):
            vals["ref"] = self.env["ir.sequence"].next_by_code(
                "hospital.patient")
            return super(HospitalPatient, self).write(vals)

    def name_get(self):
        patients_list = []
        for record in self:
            if type(record.name) == str:
                name = record.name + " " + record.ref
            else:
                name = "no name assigned  " + record.ref
            patients_list.append((record.id, name))
        return patients_list
        # return [(record.id, "%s:%s" % (record.ref, record.name)) for record in self]
