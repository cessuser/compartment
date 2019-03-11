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
                if self.session.config['negative']:
                    p.participant.vars['trts'] = random.sample([5,6,7,8], 2)
                else:
                    p.participant.vars['trts'] = random.sample([1,2,3,4],2)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    dice = models.IntegerField(min=1, max=6,
                                label="Please enter your dice value: ", widget=widgets.TextInput)
    real_dice = models.IntegerField(min=1,max=6)
    cur_trt = models.IntegerField()

    q1 = models.IntegerField(label='As a voter how would you evaluate Party Alpha, the Prime Minister’s Party, for an economy that performs above expectations? On the left is “very bad” and on the right is “very good”. ')
    q2 = models.IntegerField(label='As a voter how would you evaluate Party Beta, the Finance Minister’s Party, for an economy that performs above expectations? On the left is “very bad” and on the right is “very good”. ')
    q3 = models.IntegerField(label='As a voter how would you evaluate Party Gamma, the Minister of Foreign Affair’s Party, for an economy that performs above expectations? On the left is “very bad” and on the right is “very good”. ')
    q4 = models.StringField(choices=['Party Alpha', 'Party Beta', 'Party Gamma'], widget=widgets.RadioSelect,
                            label='4. Which of the three parties do you think is responsible for the high GDP growth rates and lower unemployment levels?')
    a1 = models.StringField(choices=['Party Alpha', 'Party Beta', 'Party Gamma'],
                            label='What party controls the Prime Ministership? Paid 100 ECUs for correct answer.', widget=widgets.RadioSelect)
    a2 = models.StringField(choices=['Party Alpha', 'Party Beta', 'Party Gamma'],
                            label='What party controls the Finance Ministry? Paid 100 ECUs for correct answer.', widget=widgets.RadioSelect)
    a3 = models.StringField(choices=['Party Alpha', 'Party Beta', 'Party Gamma'],
                            label='What party controls the Ministry of Foreign Affairs? Paid 100 ECUs for correct answer.', widget=widgets.RadioSelect)

    def set_payoff(self):
        self.payoff = Constants.dice_prize * (self.participant.vars['dice1'] + self.participant.vars['dice2'])
        if self.a1 == 'Party Alpha':
            self.payoff += 100
        if self.a2 == 'Party Beta':
            self.payoff += 100
        if self.a3 == 'Party Gamma':
            self.payoff += 100