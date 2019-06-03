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
    def is_displayed(self):
        return self.player.participant.vars['consent']

    def vars_for_template(self):
        p1 = self.player.participant.vars['n_correct1_M5'] * 100
        p2 = self.player.participant.vars['words_found'] * 100
        p3 = self.player.participant.vars['vignette']
        print(self.player.participant.vars['dice1'])
        self.player.payoff = 0
        # self.player.payoff = p1 + p2 + p3
        self.player.final_payoff = round(float(p1+p2+p3) * self.session.config['real_world_currency_per_point'],2)
        if self.session.config['UK']:
            self.player.link = '5;URL=https://cessonline.eu.qualtrics.com/jfe/form/SV_eYhSf4Ze2fVGE17?expost_uk=1&participant_label=' +\
                               str(self.player.participant.label)
        if self.session.config['Ireland']:
            self.player.link = '5;URL=https://cessonline.eu.qualtrics.com/jfe/form/SV_eYhSf4Ze2fVGE17?expost_ireland=1&participant_label=' + str(self.player.participant.label)
        return {
            'p1': p1,
            'p2': p2,
            'p3': p3,
        }

class demographic(Page):
    form_model = models.Player
    form_fields = ['age', 'gender', 'gender_other', 'student', 'edu_level', 'major', 'major_other','math_course', 'econ_course']

class Thankyou(Page):
    def is_displayed(self):
        return self.player.participant.vars['consent'] == False
page_sequence = [
    # demographic,
    Results,
    Thankyou
]
