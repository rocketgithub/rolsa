# -*- coding: utf-8 -*-
from odoo import api, models
from odoo.addons.l10n_gt_extra import a_letras

class ReportAbstractPayment(models.AbstractModel):
    _name = 'rolsa.abstract.reporte_account_payment'

    def totales(self, o):
        t = {'debito': 0, 'credito': 0}
        for l in o.move_id.line_ids:
            t['debito'] += l.debit
            t['credito'] += l.credit
        return t

    def a_letras(self,monto):
        return a_letras.num_a_letras(monto)

    def _get_report_values(self, docids, data=None):
        model = 'account.payment'
        docs = self.env['account.payment'].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'data': data,
            'a_letras': self.a_letras,
            'totales': self.totales,
        }

class ReportPayment1(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_payment1'
    _inherit = 'rolsa.abstract.reporte_account_payment'

class ReportPayment2(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_payment2'
    _inherit = 'rolsa.abstract.reporte_account_payment'

class ReportPayment3(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_payment3'
    _inherit = 'rolsa.abstract.reporte_account_payment'

class ReportPayment4(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_payment4'
    _inherit = 'rolsa.abstract.reporte_account_payment'

class ReportPayment5(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_payment5'
    _inherit = 'rolsa.abstract.reporte_account_payment'

class ReportPayment6(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_payment6'
    _inherit = 'rolsa.abstract.reporte_account_payment'

class ReportPayment7(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_payment7'
    _inherit = 'rolsa.abstract.reporte_account_payment'

class ReportPayment8(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_payment8'
    _inherit = 'rolsa.abstract.reporte_account_payment'

class ReportPayment9(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_payment9'
    _inherit = 'rolsa.abstract.reporte_account_payment'

class ReportPayment10(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_payment10'
    _inherit = 'rolsa.abstract.reporte_account_payment'
    
class ReportPayment11(models.AbstractModel):
    _name = 'report.rolsa.reporte_account_payment11'
    _inherit = 'rolsa.abstract.reporte_account_payment'
