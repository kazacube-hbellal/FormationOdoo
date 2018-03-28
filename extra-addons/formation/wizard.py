# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Wizard(models.TransientModel):
    _name = 'formation.wizard'

    def _default_session(self):
        return self.env['formation.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many('formation.session',
        string="Sessions", required=True, default=_default_session)
    participant_ids = fields.Many2many('res.partner', string="Participants")

    @api.multi
    def inscription(self):
        for session in self.session_ids:
            session.participant_ids |= self.participant_ids
        return {}

