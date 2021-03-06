# -*- coding: utf-8 -*-

from odoo import models, fields


class Country(models.Model):
    _inherit = 'res.country'

    code_iso = fields.Char('ISO Code (3 Letters)', size=3)
