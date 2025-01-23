import secrets

from odoo import fields, models


class Employe(models.Model):
    _name = "employe"
    _description = "Employé"

    name = fields.Char(string="Nom complet", required=True)
    photo = fields.Binary(string="Photo")
    gender = fields.Selection([('male', 'Masculin'), ('female', 'Féminin')], string="Sexe")
    email = fields.Char(string="Email", required = True)
    phone = fields.Char(string="Téléphone", required = True)
    date_naissance = fields.Date(string="Date de naissance")
    job_title = fields.Char(string="Poste")
    nationality = fields.Char(string="Nationalité")
    departement_id = fields.Many2one('departement', string="Département")
    responsable_id = fields.Char(string="Responsable", required = True)
    contrat_ids = fields.One2many('contrat', 'employe_id', string="Contrat")

    access_token = fields.Char("URL Token", readonly=True, default=lambda self: secrets.token_urlsafe(16))
