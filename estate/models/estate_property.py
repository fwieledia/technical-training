from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate model"

    name = fields.Char(required=True, string="Title")
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
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    user_id = fields.Many2one("res.partner", string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.users", string="Buyer", copy=False)

    def _default_date(self):
        return fields.Date.add(fields.Date.context_today(self), months=3)
