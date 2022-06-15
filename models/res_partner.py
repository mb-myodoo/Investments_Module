from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'
    
    @api.depends('investments')
    def _investments_total(self):
        for record in self:
            record.sum_investments = 0.0
            for investment in record.investments:
                record.sum_investments += investment.amount_untaxed
                   
    investments = fields.One2many('sale.order', 'investor', string='Investments', readonly= True, domain=[('state', '=', 'sale')])
    sum_investments = fields.Float('Sum of Investments', compute='_investments_total')