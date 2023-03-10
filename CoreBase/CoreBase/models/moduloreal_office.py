from odoo import fields, models

class moduloreal(models.Model):
    _name = "moduloreal.office"
    _description = "Module to REAL"

    one = fields.Char(string="1")
    two = fields.Char(string="2")
    three = fields.Char(string="3")
