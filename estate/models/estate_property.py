from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        copy=False, default=lambda self: self._default_date()
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[("n", "North"), ("s", "South"), ("e", "East"), ("w", "West")],
    )

    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ("n", "New"),
            ("r", "Offer Received"),
            ("a", "Offer Accepted"),
            ("s", "Sold"),
            ("c", "Canceled"),
        ],
        required=True,
        default="n",
        copy=False
    )

    def _default_date(self):
        return fields.Date.add(fields.Date.context_today(self), months=3)
