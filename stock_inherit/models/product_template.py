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

from odoo import models, fields

# Héritage de `stock.move.line`
class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    status = fields.Selection(
        [
            ('neuf', 'Neuf'),
            ('perdu', 'Perdu'),
        ],
        string='Status'
    )

    year = fields.Selection(
        [
            ('2000', '2000'),
            ('2010', '2010'),
        ],
        string='Année'
    )

    cartouche = fields.Char('Cartouche', required=True)

    os = fields.Selection(
        [
            ('windows_11', 'Windows 11'),
            ('windows_10', 'Windows 10'),
            ('ios', 'iOS'),
            ('android', 'Android'),
            ('macos', 'macOS'),
        ],
        string='Operating System'
    )

    description = fields.Text('Description', required=True)
    remarque = fields.Text('Remarque', required=True)

    employee_id = fields.Many2one('hr.employee', string='Employé')

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    # Champ Many2one pour relier `stock.quant` à un enregistrement `stock.move.line`
    move_line_id = fields.Many2one('stock.move.line', string="Move Line", ondelete="cascade")

    # Champs relatifs pour récupérer les données de `stock.move.line`
    status = fields.Selection(related='move_line_id.status', string="Status", store=True)
    employee_id = fields.Many2one(related='move_line_id.employee_id', string="Employé", store=True)
    year = fields.Selection(related='move_line_id.year', string="Année", store=True)
    cartouche = fields.Char(related='move_line_id.cartouche', string="Cartouche", store=True)
    os = fields.Selection(related='move_line_id.os', string="Operating System", store=True)
    description = fields.Text(related='move_line_id.description', string="Description", store=True)
    remarque = fields.Text(related='move_line_id.remarque', string="Remarque", store=True)
