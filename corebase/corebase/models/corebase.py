from odoo import fields, models

class CorebaseModule(models.Model):
    _name = "corebase.module"
    _description = "CoreBase module description"

    one = fields.Char(string="1")
    two = fields.Char(string="2")
    three = fields.Char(string="3")
