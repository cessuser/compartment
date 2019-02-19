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
    num_rounds = 1

    dice_prize = 25



class Subsession(BaseSubsession):
    treatment = models.IntegerField(min=1, max=10)

    def creating_session(self):
        self.treatment = self.session.config['treatment']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    dice1 = models.IntegerField(min=1, max=6,
                                label="Please enter your dice value: ", widget=widgets.TextInput)
    real_dice1 = models.IntegerField(min=1,max=6)
    dice2 = models.IntegerField(min=1, max=6,
                                label="Please enter your dice value: ", widget=widgets.TextInput)
    real_dice2 = models.IntegerField(min=1, max=6)
    dice3 = models.IntegerField(min=1, max=6,
                                label="Please enter your dice value: ", widget=widgets.TextInput)
    real_dice3 = models.IntegerField(min=1, max=6)
    dice4 = models.IntegerField(min=1, max=6,
                                label="Please enter your dice value: ", widget=widgets.TextInput)
    real_dice4 = models.IntegerField(min=1, max=6)
    treat = models.IntegerField()
    counts = models.IntegerField(min=1, max=10,
                             label="How many parties are in the governing coalition, i.e., in the government?"
                                   " Paid 100 ECUs for a correct answer.", widget=widgets.TextInput)
    ctlPM = models.IntegerField(choices=[(1, "Party 1"), (2, "Party 2"), (3, "Party 3")],
                             widget=widgets.RadioSelect,
                             label="What party controls the PM? Paid 100 ECUs for correct answer.")
    ctlFM = models.IntegerField(choices=[(1, "Party 1"), (2, "Party 2"), (3, "Party 3")],
                             widget=widgets.RadioSelect,
                             label="What party controls the FM? Paid 100 ECUs for correct answer.")
    ctlHC = models.IntegerField(choices=[(1, "Party 1"), (2, "Party 2"), (3, "Party 3")],
                             widget=widgets.RadioSelect,
                             label="What party controls the Health Care? Paid 100 ECUs for correct answer.")
    perfGovern = models.IntegerField(label="Based on the vignette account, how would you rate the government’s performance on this slider? On the left is “very bad” and on the right is “very good”.  Toss electronic die and report the result for payment.  You receive 25 ECUs for each die digit you report – so 25 ECU if you roll a 1; 50 ECUs if you roll a 2; up to 150 ECUs if you roll a 6.")
    perfP1 = models.IntegerField(
        label="How do you think voters would evaluate Party 1, the Prime Minister’s Party, in this example? On the left is “very bad” and on the right is “very good”. Toss electronic die and report the result for payment.  You receive 25 ECUs for each die digit you report – so 25 ECU if you roll a 1; 50 ECUs if you roll a 2; up to 150 ECUs if you roll a 6.")
    perfP2 = models.IntegerField(
        label="How do you think voters would evaluate Party 2, the Finance Minister’s Party, in this example? On the left is “very bad” and on the right is “very good”. Toss electronic die and report the result for payment.  You receive 25 ECUs for each die digit you report – so 25 ECU if you roll a 1; 50 ECUs if you roll a 2; up to 150 ECUs if you roll a 6.")

    perfP3 = models.IntegerField(
        label="How do you think voters would evaluate Party 3, the Minister of Health’s Party, in this example? On the left is “very bad” and on the right is “very good”. Toss electronic die and report the result for payment.  You receive 25 ECUs for each die digit you report – so 25 ECU if you roll a 1; 50 ECUs if you roll a 2; up to 150 ECUs if you roll a 6.")
