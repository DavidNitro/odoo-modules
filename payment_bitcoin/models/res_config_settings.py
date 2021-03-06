# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.safe_eval import safe_eval

class ResConfigSsettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    
    min_unused_bitcoin = fields.Integer('Minimun Unused Bitcoin',help='Minimum Number of Unused bitcoin address goes below this, than system send notifications to its related users.')
    
    @api.model
    def get_values(self):
        res = super(ResConfigSsettings, self).get_values()
        res.update({
            'min_unused_bitcoin': safe_eval(self.env['ir.config_parameter'].get_param('payment_bitcoin.min_unused_bitcoin', '3')),
        })
        return res
    
    @api.multi
    def set_values(self):
        super(ResConfigSsettings, self).set_values()
        self.env['ir.config_parameter'].set_param('payment_bitcoin.min_unused_bitcoin', repr(self.min_unused_bitcoin))
        