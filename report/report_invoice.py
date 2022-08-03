# -*- coding: utf-8 -*-

from odoo import api, models
import re
import odoo.addons.l10n_gt_extra.a_letras as a_letras
from datetime import date
from datetime import datetime, date, time, timedelta
import logging

class ReportAbstractInvoice(models.AbstractModel):
    _name = 'rolsa.abstract.reporte_account_invoice'

    nombre_reporte = ''

    def total_linea(self, l):
        ventas_no_sujetas = 0
        ventas_exentas = 0
        ventas_gravadas = 0
        currency = l.move_id and l.move_id.currency_id or None
        price_unit = l.price_unit * (1 - (l.discount or 0.0) / 100.0)
        taxes = l.tax_ids.compute_all(price_unit, currency, l.quantity, l.product_id, l.move_id.partner_id)
        price_total = taxes['total_included']
        timbre = 0
        if l.tax_ids:
            ventas_gravadas = l.price_subtotal
        else:
            ventas_exentas = l.price_subtotal

        return {'ventas_no_sujetas': ventas_no_sujetas,'ventas_exentas': ventas_exentas, 'ventas_gravadas': ventas_gravadas}

    def impuesto_impresos(self, o):
        impuestos = []
        iva_13 = 0
        iva_retenido_ventas = 0
        for linea in o.invoice_line_ids:
            if len(linea.tax_ids)> 0:
                precio_unitario = linea.price_unit * (100-linea.discount) / 100
                impuestos = linea.tax_ids.compute_all(precio_unitario, currency=o.currency_id, quantity=linea.quantity, product=linea.product_id, partner=o.partner_id)
                if impuestos:
                    for impuesto in impuestos['taxes']:
                        if impuesto['name'] == 'IVA por Cobrar':
                            iva_13 += impuesto['amount']
                        if impuesto['name'] == 'IVA Retenido Ventas':
                            iva_retenido_ventas += impuesto['amount']
        logging.warning({'iva_13': iva_13, 'iva_retenido_ventas': iva_retenido_ventas})
        return {'iva_13': iva_13, 'iva_retenido_ventas': iva_retenido_ventas}

    def impuestos(self,o):
        isv_15 = 0
        isv_18 = 0
        retencion = 0
        cesc_sv_5 = 0
        isv_13 = 0
        iva_por_pagar_sv = 0
        retencion_iva = 0
        for l in o.invoice_line_ids:
            precio_unitario = l.price_unit * (100-l.discount or 0.0) / 100
            impuestos = l.tax_ids.compute_all(precio_unitario, o.currency_id, l.quantity, l.product_id, l.move_id.partner_id)
            for i in impuestos['taxes']:
                if i['name'] == 'ISV por Pagar' or i['name'] == 'ISV por Cobrar':
                    isv_15 += i['amount']
                elif i['name'] == 'ISV por Pagar 18%' or i['name'] == 'ISV por Cobrar 18%':
                    isv_18 += i['amount']
                elif i['name'] == 'Retencion ISR 1%':
                    retencion += i['amount']
                elif i['name'] == 'ISV por Pagar':
                    isv_13 += i['amount']
                elif i['name'] == 'Cesc SV 5%':
                    cesc_sv_5 += i['amount']
                elif i['name'] in ['IVA por Pagar','IVA Retenido']:
                    iva_por_pagar_sv += i['amount']
                elif i['name'] == 'IVA Retenido':
                    retencion_iva += i['amount']

        return {'isv_13': isv_13,'isv_15': isv_15, 'isv_18': isv_18, 'retencion': retencion, 'cesc_sv_5': cesc_sv_5, 'iva_por_pagar_sv': iva_por_pagar_sv, 'retencion_iva': retencion_iva}

    def a_letras_dolares(self, valor):
        valor_letras = a_letras.num_a_letras(valor)
        return valor_letras + " Dolares"

    def producto(self, nombre):
        return re.sub(r'\[.+\] ', '', nombre)

    @api.model
    def _get_report_values(self, docids, data=None):
        model = 'account.move'
        docs = self.env[model].browse(docids)

        mes = a_letras.mes_a_letras(4)

        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'a_letras': a_letras.num_a_letras,
            'producto': self.producto,
            'impuesto_impresos': self.impuesto_impresos,
            'impuestos': self.impuestos,
            'a_letras_dolares': self.a_letras_dolares
        }


class ReportInvoice1(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_invoice1'
    _inherit = 'rolsa.abstract.reporte_account_invoice'

    nombre_reporte = 'rolsa.reporte_account_invoice1'

class ReportInvoice2(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_invoice2'
    _inherit = 'rolsa.abstract.reporte_account_invoice'

    nombre_reporte = 'rolsa.reporte_account_invoice6'

class ReportInvoice3(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_invoice3'
    _inherit = 'rolsa.abstract.reporte_account_invoice'

    nombre_reporte = 'rolsa.reporte_account_invoice3'

class ReportInvoice4(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_invoice4'
    _inherit = 'rolsa.abstract.reporte_account_invoice'

    nombre_reporte = 'rolsa.reporte_account_invoice4'

class ReportInvoice5(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_invoice5'
    _inherit = 'rolsa.abstract.reporte_account_invoice'

    nombre_reporte = 'rolsa.reporte_account_invoice5'

class ReportInvoice6(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_invoice6'
    _inherit = 'rolsa.abstract.reporte_account_invoice'

    nombre_reporte = 'rolsa.reporte_account_invoice6'

class ReportInvoice7(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_invoice7'
    _inherit = 'rolsa.abstract.reporte_account_invoice'

    nombre_reporte = 'rolsa.reporte_account_invoice7'
