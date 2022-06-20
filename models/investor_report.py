from odoo import api, fields, models, api, _
from datetime import date, timedelta

class InvestorReport(models.Model):
    _name = 'investor.report'
    _description = 'Investor Report'
    
    @api.depends('partner_id', 'start_date', 'end_date')
    def _get_partner_investments_list(self):

        for record in self:
            values = self.env['sale.order'].search([
                ('partner_id', '=', record.partner_id.id), ('state', '=', 'sale'),
                ('date_order', '>=', record.start_date), ('date_order', '<=', record.end_date)
            ])
            record.values = values
    
    name = fields.Char(string='Name')
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    values = fields.One2many('sale.order', 'investor', string='Value', readonly=True, compute='_get_partner_investments_list')