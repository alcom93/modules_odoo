from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand', string='Marque')
    modal_id = fields.Many2one('product.modal', string='Modèle', domain="[('brand_id', '=', brand_id)]")

    @api.onchange('brand_id')
    def _onchange_brand_id(self):
        """Clear the modal_id field when the brand_id changes."""
        if self.brand_id:
            # Clear modal_id if it doesn't belong to the selected brand
            self.modal_id = False


class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Product Brand'

    name = fields.Char('Brand Name', required=True)
    modal_ids = fields.One2many('product.modal', 'brand_id', string='Modèle')


class ProductModal(models.Model):
    _name = 'product.modal'
    _description = 'Product Modal'

    name = fields.Char('Modèle', required=True)
    brand_id = fields.Many2one('product.brand', string='Marque')


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    status = fields.Selection(
        [
            ('neuf', 'Neuf'),
            ('perdu', 'Perdu'),
        ],
        string='Status', )

    year = fields.Selection(
        [
            ('2000', '2000'),
            ('2010', '2010'),
        ],
        string='Annee', )

    cartouche = fields.Char('Cartouche', required=True)
    os = fields.Char('OS', required=True)
    description = fields.Char('Description', required=True)
    remarque = fields.Char('Remarque', required=True)

    employee_id = fields.Many2one('hr.employee', string='Employé')

