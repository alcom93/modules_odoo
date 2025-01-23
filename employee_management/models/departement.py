from odoo import fields, models

class Departement(models.Model):
    _name = "departement"
    _description = "Département"

    name = fields.Char(string="Nom du département", required=True)
    responsable_id = fields.Many2one('employe', string="Responsable du département",required=True)
    employe_ids = fields.One2many('employe', 'departement_id', string="Employés")
