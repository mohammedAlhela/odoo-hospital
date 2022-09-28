from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    confirmed_user_id = fields.Many2one("res.users"  , string = "Confirmed User")
 

    def action_confirm (self) : 
        print('test working ...........................')
        super(SaleOrder , self).action_confirm() 
