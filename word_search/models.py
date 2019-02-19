from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'David Klinowski'

doc = """
Show word search puzzle and prompt for number of words found from given list (none of which actually appear on puzzle)
as measure of cheating proclivity
"""


class Constants(BaseConstants):
    name_in_url = 'word_search'
    players_per_group = None
    num_rounds = 1

    word_puzzle_seconds = 90
    prize = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_word_search_payoff(self):
        for p in self.get_players():
            p.payoff = p.words_found


class Player(BasePlayer):
    words_found = models.PositiveIntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        widget=widgets.RadioSelect()
    )
    def set_payoff(self):
        self.payoff = self.words_found * Constants.prize
