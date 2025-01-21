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


