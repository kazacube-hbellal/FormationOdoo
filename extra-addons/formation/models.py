# -*- coding: utf-8 -*-

from openerp import models, fields


class Cours(models.Model):
    _name = 'formation.cours'

    titre = fields.Char(required=True)

    description = fields.Char()

    responsable_id = fields.Many2one('res.users', ondelete='set null',
                                     string="Responsable", index=True)

    session_ids = fields.One2many('formation.session','cours_id', string = "Sessions")


class Session(models.Model):
    _name = 'formation.session'

    nom = fields.Char(required=True)

    dateDebut = fields.Date()

    duree = fields.Float(digits=(6,2), help ="Duree en jours")

    nbPlaces = fields.Integer(string="Nombres de places")

    instructeur_id = fields.Many2one('res.partners', ondelete='set null',
                                     string="Instructeur", index=True)

    cours_id = fields.Many2one('formation.cours',
        ondelete='cascade', string="Cours", required=True)

