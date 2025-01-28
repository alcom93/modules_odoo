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
            ('2015', '2015'),
            ('2016', '2016'),
            ('2017', '2017'),
            ('2018', '2018'),
            ('2019', '2019'),
            ('2020', '2020'),
            ('2021', '2021'),
            ('2022', '2022'),
            ('2023', '2023'),
            ('2024', '2024'),
            ('2025', '2025'),
            ('2026', '2026'),
            ('2027', '2027'),
            ('2028', '2028'),
            ('2029', '2029'),
            ('2030', '2030'),

        ],
        string='Année'
    )

    cartouche = fields.Char('Cartouche', required=True)

    os = fields.Selection(
        [
            ('windows_11', 'Windows 11'),
            ('windows_10', 'Windows 10'),
            ('android', 'Android'),
            ('ios', 'ios'),
            ('macos', 'macOS'),
        ],
        string='Operating System'
    )

    description = fields.Text('Description')
    remarque = fields.Text('Remarque')

    employee_id = fields.Many2one('hr.employee', string='Employé')


    @api.model
    def _action_done(self):

        res = super(StockMoveLine, self)._action_done()

        for move_line in self:

            quants = self.env['stock.quant'].search([
                ('product_id', '=', move_line.product_id.id),
                ('location_id', '=', move_line.location_dest_id.id)
            ])

            for quant in quants:
                quant.write({
                    'move_line_id': move_line.id,  # Link quant to move line
                    'status': move_line.status,
                    'employee_id': move_line.employee_id.id,
                    'year': move_line.year,
                    'cartouche': move_line.cartouche,
                    'os': move_line.os,
                    'description': move_line.description,
                    'remarque': move_line.remarque,
                })

        return res


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
