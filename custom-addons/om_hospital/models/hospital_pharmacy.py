from odoo import fields, models


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment pharmacy lines"
    product_id = fields.Many2one(
        "product.product", string="Product", required=True)
    price_unit = fields.Float(string="Price", related="product_id.list_price")
    qty = fields.Integer(string="Quantity", default="1")
    appointment_id = fields.Many2one(
        "hospital.appointment", string="Appointment")
