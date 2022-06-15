from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'
    
    @api.depends('investments')
    def _investments_total(self):
        for record in self:
            record.sum_investments = 0.0
            for investment in record.investments:
                record.sum_investments += investment.amount_untaxed
                
    @api.depends('sale.order')
    def _so_list(self):
        for record in self:
            
        
                
    
    investments = fields.One2many('sale.order', 'investor', string='Investments', readonly=True, compute='_so_list')
    sum_investments = fields.Float("Sum of Investments", compute='_investments_total')
