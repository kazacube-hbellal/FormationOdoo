# -*- coding: utf-8 -*-

from openerp import models, fields

from openerp import api


class Cours(models.Model):
    _name = 'formation.cours'
    _rec_name = 'titre'

    titre = fields.Char(required=True)

    description = fields.Char()

    responsable_id = fields.Many2one('res.users', ondelete='set null',
                                     string="Responsable", index=True)

    session_ids = fields.One2many('formation.session','cours_id', string = "Sessions")


class Session(models.Model):
    _name = 'formation.session'

    nom = fields.Char(required=True)

    dateDebut = fields.Date(default=fields.Date.today)

    duree = fields.Float(digits=(6,2), help ="Duree en jours")

    nbPlaces = fields.Integer(string="Nombres de places")

    active = fields.Boolean(default=True)

    instructeur_id = fields.Many2one('res.partner', ondelete='set null',
                                     string="Instructeur", index=True,
                                     domain=[('instructor', '=', True)])

    cours_id = fields.Many2one('formation.cours',
        ondelete='cascade', string="Cours", required=True)

    participant_ids = fields.Many2many('res.partner',string="Participants")

    places_occupees = fields.Float(string="Places occupees", compute='_places_occupees')

    @api.depends('nbPlaces', 'participant_ids')
    def _places_occupees(self):
        for r in self:
            if not r.nbPlaces:
                r.places_occupees = 0.0
            else:
                r.places_occupees = 100.0 * len(r.participant_ids) / r.nbPlaces

