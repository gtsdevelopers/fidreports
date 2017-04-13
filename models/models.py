# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class myreports(models.Model):
#     _name = 'myreports.myreports'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class button_invoices(models.Model):
    _name = 'button.invoicess'
    name = fields.Char(required=True,default='Click to generate name!')
    report = fields.TEXT(compute='listInvoices()', string='Invoice Report List')
    
    """ out_invoice is customer invoice, not vendor bill"""
    def listInvoices(self,mydate,invtype):
        """ List all customer invoices greater than mydate
           invtype is 'out_invoice' for Customer invoice or 'in_invoice' for vendor bills
        """
        account_invoice_obj = self.env['account.invoice'].search([('date_invoice', '>', mydate), \
                                                     ('type','=',invtype)])
        prt = 'Date,Customer,SalesPerson,product,qty,unitprice\n'
        prtl = ""
        for invoice in account_invoice_obj:
            lenlines = len(invoice.invoice_line_ids)
            if invoice.date_invoice  and lenlines > 0:
                prt = prt + str(invoice.date_invoice) + ',' + str(invoice.partner_id.name) +','+ str(invoice.user_id.name) +','+ str(invoice.invoice_line_ids[0].name) + ',' + str(invoice.invoice_line_ids[0].quantity) \
                + ',' + str(invoice.invoice_line_ids[0].price_unit) + '\n'    
                lenlines = len(invoice.invoice_line_ids)
                prtl = ""
                for k in range(1,lenlines-1):
                    prtl = ',,,' + str(invoice.invoice_line_ids[k].name) + ',' + str(invoice.invoice_line_ids[k].quantity) \
                    + ',' + str(invoice.invoice_line_ids[k].price_unit) + '\n'
                    prt = prt + prtl
        return prt 
    