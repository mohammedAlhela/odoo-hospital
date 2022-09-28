from multiprocessing import context
from odoo import api,  fields, models, _
import datetime
from odoo.exceptions import ValidationError


class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = " Cancel Appointments."

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res["cancel_date"] = datetime.date.today()
        res["appointment_id"] = self.env.context.get("active_id")
        return res

    appointment_id = fields.Many2one(
        "hospital.appointment",  string="Appointment")
    reason = fields.Text(string="Reason")
    cancel_date = fields.Datetime(string="Cancelling Date")

    def cancel_appointment(self):
        # if self.appointment_id.booking_date == datetime.date.today():
        raise ValidationError(
                "You cant cancel the appointment on the same date of booking it")

