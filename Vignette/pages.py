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
        if self.player.cur_trt < 5:
            self.player.treatment_label = 'T3' + str(self.player.cur_trt)
        else:
            self.player.treatment_label = 'T4' + str(self.player.cur_trt - 4)

class trt1_2(Page):
    form_model = models.Player
    form_fields = ['q1', 'q2', 'q3', 'q4']


class trt1_3(Page):
    def before_next_page(self):
        self.player.real_die_value = random.randint(1,6)

    def dice_error_message(self, value):
        if value > 6 or value < 1:
            return 'Invalid value! To continue, please roll the dice again, and enter a value between 1 and 6! '

    def real_dice_error_message(self,value):
        if value == '':
            return "Please make sure your dice is rolled."

class additionals(Page):
    form_fields = ['a1', 'a2', 'a3']
    form_model = models.Player

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def before_next_page(self):
        self.player.set_payoff()
        self.player.participant.vars['vignette'] = self.player.payoff

class trt1_3_1(Page):
    form_model = models.Player
    form_fields = ['dice']

    def before_next_page(self):
        if self.round_number == 1:
            self.player.participant.vars['dice1'] = []
        self.player.participant.vars['dice1'].append(self.player.dice)

    def dice_error_message(self, value):
        if value > 6 or value < 1:
            return 'Invalid value! Please enter a value between 1 and 6! '


page_sequence = [
    Introduction,
    trt1_1,
    trt1_2,
    trt1_3,
    trt1_3_1,
    additionals,
    # Results
]
