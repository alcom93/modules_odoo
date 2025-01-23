
from odoo import http
from odoo.http import request

class EmployeeBadgeController(http.Controller):

    @http.route('/employee/badge/<string:token>', type='http', auth='public', website=True)
    def generate_employee_badge(self, token, **kwargs):

        employee = request.env['employe'].sudo().search([('access_token', '=', token)], limit=1)

        if not employee:
            return request.not_found()

        return request.render('employe_management.fiche_report_template', {
            'employe': employee,
        })
