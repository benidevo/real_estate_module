from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(required=True, )
    description = fields.Text()
    post_code = fields.Char()
    date_availability = fields.Datetime("Date Availability",
                                        default=lambda self: fields.Datetime.now())
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string="Type",
        selection=[("north", "North"), ("south", "South"),
                   ("east", "East"), ("west", "West")],
        help="This is used to select the garden orientation"
    )
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string="State",
        selection=[("New", "New"), ("Offer Received", "Offer Received"),
                   ("Offer Received", "Offer Accepted"), ("Sold", "Sold"), ("Canceled", "Canceled")],
        required=True,
        copy=False,
        default="New"
    )
