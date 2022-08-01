# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"

    centro_negocio = fields.Char('Centro de negocio')
    numero_order_compra = fields.Char('Número de orden de compra')
    numero_recepcion_aceptacion = fields.Char('No. Recepción / Aceptación')

class AccountJournal(models.Model):
    _inherit = "account.journal"

    cai = fields.Char('C.A.I.')
    numero_desde = fields.Char('Número desde')
    numero_hasta = fields.Char('Número hasta')
    fecha_limite = fields.Date('Fecha límite de emisión')
