from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property.tag"
    _description = "estate tag"

    name = fields.Char(required=True)