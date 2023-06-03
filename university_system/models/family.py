from odoo import models, fields


class FamilyMembers(models.Model):
    _name = "family.member"
    _description = "Family Members"

    _rec_name = 'family_member_name'
    _order = 'family_member_name ASC'


    family_member_name = fields.Char(
        string="Name",
        tracking=True
    )
    family_member_age = fields.Integer(
        string="Age",
        tracking=True
    )
