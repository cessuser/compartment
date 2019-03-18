from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import  models

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    def vars_for_template(self):
        p1 = self.player.participant.vars['n_correct1_M5'] * 150
        p2 = self.player.participant.vars['words_found'] * 100
        p3 = self.player.participant.vars['vignette']
        print(self.player.participant.vars['dice1'])
        self.player.payoff = p1 + p2 + p3
        self.player.final_payoff = round(float(self.player.payoff * self.session.config['real_world_currency_per_point']),2)
        return {
            'p1': p1,
            'p2': p2,
            'p3': p3
        }

class demographic(Page):
    form_model = models.Player
    form_fields = ['age', 'gender', 'gender_other', 'student', 'edu_level', 'major', 'major_other','math_course', 'econ_course']

page_sequence = [
    demographic,
    Results
]
