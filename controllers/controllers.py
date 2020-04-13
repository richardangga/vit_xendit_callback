# -*- coding: utf-8 -*-
from odoo import http
import simplejson
import time
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)


class VitXenditCallback(http.Controller):
    @http.route('/xendit/invoice/paid', auth='public')
    def index(self, **kw):
        _logger.info(kw)
        # external = kw.get('external')
        # sale_order = request.env['sale.order'].search([('external','=',external)])
        # if not sale_order:
        #     res = {'status':'FAILED', 'message':'SO not found'}
        #     return simplejson.dumps(res)
        # journal_id = request.env['account.journal'].search([('name','=','Bank')])
        # payment_method= request.env['account.payment.method'].search([('code','=','electronic')])
        payment = request.env['account.payment'].search(['external','=','external_id'])
        payment.create({
            'payment_type':'inbound',
            'partner_type':'customer',
            'partner_id': 'user_id',
            'amount': 'amount',
            'journal_id': 'external_id' ,
            'payment_date': 'paid_at',
            'communication': 'description' ,
            'payment_method_id' : 'payment_method'
        })
        # p.post()
        # res = {'message': 'success'}
        # res = {
        #     'id': sale_order.id_xendit,
        #     'external_id': sale_order.external,
        #     'user_id': sale_order.user_xendit,
        #     'is_high': 'true',
        #     'payment_method': 'BANK_TRANSFER',
        #     'status': 'PAID',
        #     'merchant_name': sale_order.name,
        #     'amount': sale_order.amount_untaxed,
        #     'paid_amount': sale_order.amount_total,
        #     'bank_code': 'PERMATA',
        #     'paid_at': time.strftime('%Y-%m-%d'),
        #     'payer_email': sale_order.email,
        #     'description': sale_order.account_so_url + '' + sale_order.merchant,
        #     'adjusted_received_amount': sale_order.amount_type_pay,
        #     'fees_paid_amount': sale_order.amount_type_pay,
        #     'updated': sale_order.write_date,
        #     'created': sale_order.created,
        #     'currency': 'IDR',
        #     'payment_channel': 'PERMATA',
        #     'payment_destination': '888888888888'
        #     }
        return simplejson.dumps(res)
        print(res)

    # @http.route('/xendit/fva/paid', method='POST', auth='public')
    # def index(self, **kw):
    #     _logger = info(kw)
    #     va_number = kw.get('va_number')
    #     res_partner = request.env['res.partner'].search([('va_number','=',va_number)])
    #     if not res_partner:
    #         rest = {'status':'FAILED', 'message':'SO not found'}
    #         return simplejson.dumps(rest)
    #     journal_id = request.env['account.journal'].search([('name','=','Bank')])
    #     payment_method= request.env['account.payment.method'].search([('code','=','electronic')])
    #     payment = request.env['account.payment']
    #     p = payment.create({
    #         'payment_type':'inbound',
    #         'partner_type':'customer',
    #         'partner_id': res_partner.id,
    #         'amount': res_partner.amount,
    #         'journal_id': journal_id.id ,
    #         'payment_date': time.strftime('%Y-%m-%d'),
    #         'communication': 'XENDIT ' + res_partner.partner_res_id ,
    #         'payment_method_id' : payment_method.id
    #     })
    #     p.post()

        # res = {
        #     "updated": res_partner.write_date,
        #     "created": res_partner.write_date,
        #     # "payment_id": ,
        #     "callback_virtual_account_id": "58a434ba39cc9e4a230d5a2b",
        #     "owner_id": res_partner.owner_res_id,
        #     "external_id": res_partner.va_external_id,
        #     "account_number": res_partner.va_number,
        #     "bank_code": res_partner.va_bank,
        #     "amount": res_partner.amount,
        #     "transaction_timestamp": res_partner.expiration_date_xendit,
        #     "merchant_code": res_partner.merchant_code,
        #     "id": res_partner.partner_res_id
        #     }
        # res = {'message': 'success'}
        # return simplejson.dumps(res)
        # print(res)

#     @http.route('/vit_xendit_callback/vit_xendit_callback/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_xendit_callback.listing', {
#             'root': '/vit_xendit_callback/vit_xendit_callback',
#             'objects': http.request.env['vit_xendit_callback.vit_xendit_callback'].search([]),
#         })

#     @http.route('/vit_xendit_callback/vit_xendit_callback/objects/<model('vit_xendit_callback.vit_xendit_callback'):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_xendit_callback.object', {
#             'object': obj
#         })