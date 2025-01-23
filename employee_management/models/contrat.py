from odoo import models, fields


class Contrat(models.Model):
    _name = "contrat"
    _description = "Contrat"

    name = fields.Selection(selection=[('cdd', 'CDD'), ('cdi', 'CDI'), ('stage', 'Stage')], string="Type de contrat",
                            required=True)
    date_debut = fields.Date(string="Date de début", required=True)
    date_fin = fields.Date(string="Date de fin")
    employe_id = fields.Many2one('employe', string="Employé")
    file_contrat = fields.Binary(string="Le contrat", required = True)


