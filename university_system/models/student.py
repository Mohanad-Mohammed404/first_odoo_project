# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class StudentData(models.Model):
    _name = "student.data"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Student Data"

    _rec_name = "stud_name"

    stud_name = fields.Char(
        string="Student Name",
        required=True,
        tracking=True
    )
    nat_id = fields.Char(
        string="National ID",
        required=True,
        tracking=True
    )
    stud_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')],
        string="Gender",
        required=True,
        tracking=True
    )
    ad_country = fields.Char(
        string="Country",
        required=True,
        tracking=True
    )
    ad_city = fields.Char(
        string="City",
        required=True,
        tracking=True
    )
    ad_street = fields.Char(
        string="Street",
        required=True,
        tracking=True
    )
    stud_image = fields.Image(
        string="Student Image"
    )
    sec_certificate_image = fields.Image(
        string="Secondary Certificate Image"
    )
    stud_degree = fields.Integer(
        string="Secondary Degree",
        tracking=True
    )
    stud_percentage = fields.Integer(
        string="Secondary Percentage",
        tracking=True
    )
    birth_date = fields.Date(
        string="Birth Date",
        required=True,
        tracking=True
    )
    age = fields.Integer(
        string="Age",
        compute="_compute_age",
        readonly=True
    )
    stud_height = fields.Integer(
        string="Student Height (M)",
        tracking=True
    )
    stud_weight = fields.Integer(
        string="Student Weight (Kg)",
        tracking=True
    )
    family_count = fields.Integer(
        string="Family members count",
        tracking=True
    )
    family_id = fields.Many2many(
        "family.member",
        string="Family Members",
        tracking=True
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birth_date:
                rec.age = today.year - rec.birth_date.year
            else:
                rec.age = 0

    @api.constrains('nat_id')
    def _check_nat_digits(self):
        for rec in self:
            if not rec.nat_id.isdigit() or len(rec.nat_id) != 14:
                raise ValidationError("National ID should contain exactly 14 digits")
