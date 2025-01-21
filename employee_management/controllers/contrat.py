from odoo import http
from odoo.http import request

class ContratReportController(http.Controller):
    @http.route('/api/contrat/pdf/<int:contrat_id>', auth='public', type='http', csrf=False)
    def get_contrat_pdf(self, contrat_id):
        """
        Retourne un PDF généré pour un contrat spécifique.
        """
        # Récupérer le contrat
        contrat = request.env['employe.management.contrat'].sudo().search([('id', '=', contrat_id)], limit=1)
        if not contrat:
            return request.not_found()

        # Générer le PDF
        pdf = request.env.ref('employe_management.contrat_report_template').sudo()._render_qweb_pdf([contrat_id])[0]

        # Configurer les en-têtes HTTP pour retourner un PDF
        pdf_http_headers = [
            ('Content-Type', 'application/pdf'),
            ('Content-Length', len(pdf)),
            ('Content-Disposition', f'inline; filename=contract_{contrat_id}.pdf'),
        ]
        return request.make_response(pdf, headers=pdf_http_headers)
