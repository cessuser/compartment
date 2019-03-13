from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'David Klinowski Danlin Chen'

doc = """
Show word search puzzle and prompt for number of words found from given list (none of which actually appear on puzzle)
as measure of cheating proclivity

number of choices changed, puzzle picture changed
"""


class Constants(BaseConstants):
    name_in_url = 'word_search'
    players_per_group = None
    num_rounds = 1

    word_puzzle_seconds = 30
    prize = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_word_search_payoff(self):
        for p in self.get_players():
            p.payoff = p.words_found


class Player(BasePlayer):
    cows_found = models.IntegerField(min=0, max=100,choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])

    def set_payoff(self):
        self.payoff = self.cows_found * Constants.prize
