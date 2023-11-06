from odoo import models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate tag"

    price = fields.Float()
    status = fields.Selection(
        selection=[
            ("a", "Accepted"),
            ("r", "Refused")
        ],
        copy=False
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)