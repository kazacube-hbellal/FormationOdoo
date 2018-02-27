# -*- coding: utf-8 -*-
from openerp import http

# class Formation(http.Controller):
#     @http.route('/formation/formation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formation/formation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('formation.listing', {
#             'root': '/formation/formation',
#             'objects': http.request.env['formation.formation'].search([]),
#         })

#     @http.route('/formation/formation/objects/<model("formation.formation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formation.object', {
#             'object': obj
#         })