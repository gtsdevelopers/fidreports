# -*- coding: utf-8 -*-
from openerp import http

# class Myreports(http.Controller):
#     @http.route('/myreports/myreports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myreports/myreports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myreports.listing', {
#             'root': '/myreports/myreports',
#             'objects': http.request.env['myreports.myreports'].search([]),
#         })

#     @http.route('/myreports/myreports/objects/<model("myreports.myreports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myreports.object', {
#             'object': obj
#         })