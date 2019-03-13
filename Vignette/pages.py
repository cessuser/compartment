from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import random

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        self.player.payoff = 0



class trt1_1(Page):
    def vars_for_template(self):
        self.player.cur_trt = self.player.participant.vars['trts'][self.round_number-1]


class trt1_2(Page):
    form_model = models.Player
    form_fields = ['q1', 'q2', 'q3', 'q4']

class trt1_3(Page):
    form_model = models.Player
    form_fields = ['dice', 'real_dice']

    def before_next_page(self):
            self.player.participant.vars['dice1'] = self.player.dice


class Results(Page):
    def is_displayed(self):
        return  self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.set_payoff()
        p1 = self.player.participant.vars['n_correct1_M5'] * 150
        p2 = self.player.participant.vars['words_found'] * 100

        return {
            'p1': p1,
            'p2': p2,

        }

class additionals(Page):
    form_fields = ['a1', 'a2', 'a3']
    form_model = models.Player
    def is_displayed(self):

        return  self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.set_payoff()
        self.player.participant.vars['vignette'] = self.player.payoff

page_sequence = [
    Introduction,
    trt1_1,
    trt1_2,
    trt1_3,
    additionals,
    # Results
]
