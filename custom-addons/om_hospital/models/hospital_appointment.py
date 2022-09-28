from odoo import api, fields, models


class HospitalAppointment(models.Model):
    """
    Manage Hospital Appointments.
    """
    _name = "hospital.appointment"
    _description = "Managing Hospital Appointments."
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # String fields:
    active = fields.Boolean("Active", default=True)
    patient_id = fields.Many2one("hospital.patient", string="Patient")
    booking_date = fields.Date(
        "Booking Date", default=fields.Date.context_today)
    booking_time = fields.Datetime("Booking Time", default=fields.Datetime.now)
    gender = fields.Selection("Gender", related="patient_id.gender")
    ref = fields.Char("Reference")
    prescription = fields.Html("Prescription")
    doctor_id = fields.Many2one("res.users", string="Doctor")
    hide_sale_price = fields.Boolean(string="Hide Pharmacy Sale Price")
    pharmacy_ids = fields.One2many("appointment.pharmacy.lines", "appointment_id", string="Pharmacies")
    priority = fields.Selection(
        [("1", "Low"),
         ("2", "Medium"),
         ("3", "Heigh"),
         ],
        "Priority",
    )

    state = fields.Selection(
        [("draft", "Draft"),
         ("open", "Open"),
         ("done", "Done"),
         ("cancel", "Cancel"),
         ],
        string="State",
        required=True,
        default="draft",
        tracking=True

    )

    @api.onchange("patient_id")
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def init_rainbow(self):
        return {
            "effect":  {
                "fadeout": "slow",
                "message": "dont forget to controll yourself",
                "type": "rainbow_man",
            }
        }

    def state_open(self):
        for rec in self:
            rec.state = "open"


    def state_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def state_draft(self):
        for rec in self:
            rec.state = "draft"

    def state_done(self):
        for rec in self:
            rec.state = "done"

    def name_get(self):
        appointment_list = []
        for record in self:
            appointment_list.append((record.id, record.ref))
        return appointment_list
           
