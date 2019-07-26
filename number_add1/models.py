from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
author = 'Danlin Chen'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'number_add1'
    players_per_group = None
    num_rounds = 30
    prize = 100

    nums1 = [65, 16, 37, 59, 76, 48, 12, 60, 73, 96, 29, 89, 31, 29, 31, 95, 71, 46, 61, 20, 15, 37, 68, 67, 52, 91, 74,
             52, 47, 44]
    nums2 = [33, 73, 81, 97, 58, 92, 47, 10, 47, 49, 94, 18, 71, 14, 53, 90, 61, 28, 78, 48, 21, 78, 95, 33, 92, 10, 18,
             63, 100, 65]

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['nums1'] = Constants.nums1
            p.participant.vars['nums2'] = Constants.nums2
            p.participant.vars['ans'] = []
            for i in range(0,Constants.num_rounds):
                p.participant.vars['ans'].append(Constants.nums1[i] + Constants.nums2[i])
                if self.round_number == 1:
                    p.participant.vars['M5_round1Pay'] = 0
                    p.participant.vars['n_correct1_M5'] = 0


class Group(BaseGroup):
    def set_payoff(self):
        player_sorted = [[p, p.participant.vars['n_correct1_M5']] for p in self.get_players()]

        for pair in player_sorted:
            pair[0].payoff = pair[1] * Constants.prize

class Player(BasePlayer):
    consent = models.BooleanField(widget=widgets.RadioSelect,
                                 label='Bent u het eens met de bovenstaande informatie?',
                                 choices=[(True, 'Ja'), (False, 'Nee')])
    label = models.StringField()
    answer = models.IntegerField(label='Antwoord:') # player answer
    correct = models.IntegerField() # if correct
    n_correct = models.IntegerField() # number of correct
    modelPred = models.IntegerField(choices=[(1, '1st place'), (2, '2nd place'), (3, 'Bottom')], widget=widgets.RadioSelect)
    roundPred = models.IntegerField(choices=[1, 2, 3], widget=widgets.RadioSelect)

    rank = models.IntegerField()


    def set_label(self):
        self.label = self.participant.label

    def check_correct(self):
        if self.round_number == 1:
            self.participant.vars['n_correct1_M5'] = 0
        if self.answer == Constants.nums1[self.round_number-1] + Constants.nums2[self.round_number-1]:
            self.correct = 1
            self.participant.vars['n_correct1_M5'] += 1
        else:
            self.correct = 0
        self.n_correct = self.participant.vars['n_correct1_M5']


