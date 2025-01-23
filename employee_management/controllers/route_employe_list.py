from odoo import http
from odoo.http import request

class EmployeePortal(http.Controller):

    @http.route('/my/employees', type='http', auth='public', website=True)
    def employee_list(self, **kwargs):

        employees = request.env['employe'].sudo().search([])

        return request.render('employe_management.employees_list', {
            'employe': employees,
            'page_name': 'employees_list'
        })

    @http.route('/my/employees/<string:token>', type='http', auth='public', website=True)
    def generate_employee_details(self, token, **kwargs):
        employe = request.env['employe'].sudo().search([('access_token', '=', token)], limit=1)


        return request.render('employe_management.employees_details', {
            'employe': employe,
            'page_name': 'employees_details'
        })