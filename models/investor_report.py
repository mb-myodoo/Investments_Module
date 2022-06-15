from odoo import api, fields, models, api, _


class InvestorReport(models.Model):
    _name = 'investor_report'
    _description = 'Investor Report'
    
    name = fields.Char(string='Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    values = fields.One2many('sale.order', 'investor', string='Value')