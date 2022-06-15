from odoo import api, fields, models, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    investor = fields.Many2one('res.partner', string='Investor')
    
    @api.constrains('investor', 'partner_id')
    def _check_investor(self):
        for record in self: 
            if record.investor == record.partner_id:
                raise ValidationError(_('Client and Investor cann"t be the same'))