from odoo import models, fields, api
from odoo.exceptions import ValidationError

class FacultyDesire(models.Model):
    _name="faculty.desire"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description="Faculty Desire"
    _rec_name="stud_id"

    stud_id= fields.Many2one(
        "student.data",
        string="Student Name"
    )
    stud_image= fields.Image(related="stud_id.stud_image")
    nat_id= fields.Char(
        string="National ID"
    )
    gender= fields.Selection(related="stud_id.stud_gender")
    exp_college= fields.Selection([
        ('medicine', 'Faculty of Medicine'),
        ('engineering', 'Faculty of Engineering'),
        ('commerce', 'Faculty of Commerce'),
        ('science', 'Faculty of Science'),
        ('law', 'Faculty of Law'),
        ('arts', 'Faculty of Arts'),
        ('dentistry', 'Faculty of Dentistry'),
        ('pharmacy', 'Faculty of Pharmacy'),
        ('agriculture', 'Faculty of Agriculture'),
        ('education', 'Faculty of Education')
    ],
        required=True,
        tracking=True,
    string="Expected College"
    )
    desire_college= fields.Selection([
        ('medicine', 'Faculty of Medicine'),
        ('engineering', 'Faculty of Engineering'),
        ('commerce', 'Faculty of Commerce'),
        ('science', 'Faculty of Science'),
        ('law', 'Faculty of Law'),
        ('arts', 'Faculty of Arts'),
        ('dentistry', 'Faculty of Dentistry'),
        ('pharmacy', 'Faculty of Pharmacy'),
        ('agriculture', 'Faculty of Agriculture'),
        ('education', 'Faculty of Education')
    ],
        required=True,
        tracking=True,
    string="Desire College"
    )

    reson= fields.Char(
        string="The reason for the college need",
        tracking=True
    )

    stud_skills= fields.Text(
        string="Skills",
        tracking=True
    )
    stud_talent = fields.Text(
        string="Talents",
        tracking=True
    )

    @api.onchange('stud_id')
    def _onchange_stud_id(self):
        self.nat_id = self.stud_id.nat_id

    @api.constrains('nat_id')
    def _check_nat_digits(self):
        for rec in self:
            if not rec.nat_id.isdigit() or len(rec.nat_id) != 14:
                raise ValidationError("National ID should contain exactly 14 digits")