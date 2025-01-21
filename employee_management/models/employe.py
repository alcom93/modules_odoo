from odoo import fields, models

class Employe(models.Model):
    _name = "employe"
    _description = "Employé"

    name = fields.Char(string="Nom complet", required=True)
    email = fields.Char(string="Email", required = True)
    phone = fields.Char(string="Téléphone", required = True)
    date_naissance = fields.Date(string="Date de naissance")
    departement_id = fields.Many2one('departement', string="Département")
    responsable_id = fields.Char(string="Responsable", required = True)
    contrat_ids = fields.One2many('contrat', 'employe_id', string="Contrat")


