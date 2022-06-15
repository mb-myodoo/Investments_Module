from odoo import api, fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    investor = fields.Many2one('res.partner', string='Investor', help='Name of Investor')