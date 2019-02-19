from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models


class Introduction(Page):
    def vars_for_template(self):
        self.player.payoff = 0


class Questions(Page):
    form_model = models.Player
    form_fields = ['counts', 'ctlPM','ctlFM','ctlHC']

    def before_next_page(self):
        if self.player.counts == 3:
            self.player.payoff += 100
        if self.player.ctlPM == 1:
            self.player.payoff += 100
        if self.player.ctlFM == 2:
            self.player.payoff += 100
        if self.player.ctlHC == 3:
            self.player.payoff += 100

class Questions1(Page):
    form_model = models.Player
    form_fields = ['perfGovern', 'dice1','real_dice1']

    def before_next_page(self):
        self.player.payoff += self.player.dice1 * Constants.dice_prize


class Questions2(Page):
    form_model = models.Player
    form_fields = ['perfP1', 'dice2', 'real_dice2']

    def before_next_page(self):
        self.player.payoff += self.player.dice2 * Constants.dice_prize


class Questions3(Page):
    form_model = models.Player
    form_fields = ['perfP2', 'dice3','real_dice3']

    def before_next_page(self):
        self.player.payoff += self.player.dice3 * Constants.dice_prize

class Questions4(Page):
    form_model = models.Player
    form_fields = ['perfP3', 'dice4', 'real_dice4']

    def before_next_page(self):
        self.player.payoff += self.player.dice4 * Constants.dice_prize


page_sequence = [
    Introduction,
    Questions,
    Questions1,
    Questions2,
    Questions3,
    Questions4
]
