from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Danlin Chen'

doc = """
4 Treatments: Low, High, Economy good, Economy bad
"""


class Constants(BaseConstants):
    name_in_url = 'Vignette'
    players_per_group = None
    num_rounds = 2

    dice_prize = 25




class Subsession(BaseSubsession):
    treatment = models.IntegerField(min=1, max=10)

    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['trts'] = [random.choice([5,6,7,8])]
                p.participant.vars['trts'].append(random.choice([1,2,3,4]))
                random.shuffle(p.participant.vars['trts'])

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    dice = models.IntegerField(label="Voer uw dobbelwaarde in:", widget=widgets.TextInput)
    real_die_value = models.IntegerField(min=1, max=6)
    cur_trt = models.IntegerField()
    treatment_label = models.StringField()


    q1 = models.IntegerField(label='Als kiezer, hoe zou u partij Alpha, van de Minister President, beoordelen, bij een economie die boven de verwachtingen presteert? Links is “erg slecht” en rechts is “erg goed”.')
    q2 = models.IntegerField(label=' Als kiezer, hoe zou u partij Beta, van de Minister van Financiën, beoordelen, bij een economie die boven de verwachtingen presteert? Links is “erg slecht” en rechts is “erg goed”.')
    q3 = models.IntegerField(label='Als kiezer, hoe zou u partij Gamma, van de Minister van Buitenlandse Zaken, beoordelen, bij een economie die boven de verwachtingen presteert? Links is “erg slecht” en rechts is “erg goed”.')
    q4 = models.StringField(choices=['Partij Alpha', 'Partij Beta', 'Partij Gamma'], widget=widgets.RadioSelect,
                            label='4.Welke van de drie partijen vindt u hoofdzakelijk verantwoordelijk voor de hoge BBP groei en het lagere werkloosheidsniveau?')
    a1 = models.StringField(choices=['Partij Alpha', 'Partij Beta', 'Partij Gamma'],
                            label='Tot welke partij behoort de Minister President? U verdient 100 ECUs voor het correcte antwoord.', widget=widgets.RadioSelect)
    a2 = models.StringField(choices=['Partij Alpha', 'Partij Beta', 'Partij Gamma'],
                            label='Tot welke partij behoort de Minister van Financiën? U verdient 100 ECUs voor het correcte antwoord. ', widget=widgets.RadioSelect)
    a3 = models.StringField(choices=['Partij Alpha', 'Partij Beta', 'Partij Gamma'],
                            label='Tot welke partij behoort de Minister van Buitenlandse Zaken? U verdient 100 ECUs voor het correcte antwoord.', widget=widgets.RadioSelect)

    def set_payoff(self):
        self.payoff = Constants.dice_prize * sum(self.participant.vars['dice1'])
        if self.a1 == 'Partij Alpha':
            self.payoff += 100
        if self.a2 == 'Partij Beta':
            self.payoff += 100
        if self.a3 == 'Partij Gamma':
            self.payoff += 100
