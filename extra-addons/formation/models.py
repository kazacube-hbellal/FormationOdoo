# -*- coding: utf-8 -*-

from openerp import models, fields

from openerp import api

from datetime import datetime, timedelta


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
    _rec_name = 'nom'

    nom = fields.Char(required=True)

    dateDebut = fields.Date(string="Date de debut",default=fields.Date.today)

    duree = fields.Float(digits=(6,2), help ="Duree en jours")

    dateFin = fields.Date(string="Date de fin")

    nbPlaces = fields.Integer(string="Nombres de places")

    active = fields.Boolean(default=True)

    instructeur_id = fields.Many2one('res.partner', ondelete='set null',
                                     string="Instructeur", index=True,
                                     domain=[('instructor', '=', True)])

    cours_id = fields.Many2one('formation.cours',
        ondelete='cascade', string="Cours", required=True)

    participant_ids = fields.Many2many('res.partner',string="Participants")

    places_occupees = fields.Float(string="Places occupees", compute='_places_occupees')

    @api.onchange('duree')
    def _set_dateFin(self):
        fmt = '%Y-%m-%d'
        dateDebut = datetime.strptime(self.dateDebut,fmt)
        duree = int(self.duree)
        dateFin = dateDebut + timedelta(days=duree)
        self.dateFin = str(dateFin)

    @api.onchange('dateFin','dateDebut')
    def _set_Duree(self):
        fmt = '%Y-%m-%d'
        dateDebut = datetime.strptime(self.dateDebut,fmt)
        dateFin = datetime.strptime(self.dateFin,fmt)
        duree = str((dateFin-dateDebut).days)
        self.duree = float(duree)


    @api.depends('nbPlaces', 'participant_ids')
    def _places_occupees(self):
        for r in self:
            if not r.nbPlaces:
                r.places_occupees = 0.0
            else:
                r.places_occupees = 100.0 * len(r.participant_ids) / r.nbPlaces

    @api.onchange('nbPlaces', 'participant_ids')
    def _verifier_places_valides(self):
        if self.nbPlaces < 0:
            return {
                'warning': {
                    'title': "Nombre de places incorrect",
                    'message': "Le nombre de places ne peut etre inferieur a zero",
                },
            }
        if self.nbPlaces < len(self.participant_ids):
            return {
                'warning': {
                    'title': "Trop de participants",
                    'message': "Augmentez le nombre de places ou supprimer des participants",
                },
            }

