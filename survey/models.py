from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'danlin chen'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    link = models.StringField()
    age = models.IntegerField(min=18, max=100, label="leeftijd:")
    gender = models.StringField(choices=['man', 'vrouw', 'anders'], label="geslacht:", widget=widgets.RadioSelect)
    edu_level = models.StringField(
        label="Selecteer uw hoogst genoten vorm van onderwijs van de onderstaande categorieën",
              choices=['Geen formeel onderwijs',
                       'Basisschool',
                       'Vmbo',
                       'Havo',
                       'Vwo',
                       'Mbo',
                       'Hogeschool bachelor',
                       'Universiteit bachelor',
                       'Hogeschool master',
                       'Universiteit master','PhD'], widget=widgets.RadioSelect)
    ethnicity = models.StringField(
        label="Kies een of meer etnische achtergronden waar u uzelf bij vindt horen:",
        choices=['Blank','Gemengd/meerdere Etnische groepen','Turks (Turkish)','Marokkaans  (Moroccan)','Nederlandsche Antillen (Dutch Antilles)','Anders (Other)'],
        widget=widgets.RadioSelect)
    household_income = models.StringField(
        label='Wat is het totale inkomen van uw huishouden per jaar?',
        choices=['Minder dan 10.000 Euro',
                 '10.000 tot 20.000 Euro',
                 '20.000 tot 30.000 Euro',
                 '30.000 tot 40.000 Euro',
                 '40.000 tot 50.000 Euro',
                 '100.000 tot 200.000 Euro',
                 '200.000 Euro of meer',
                 'Zeg ik liever niet'],
        widget=widgets.RadioSelect
    )
    comments = models.StringField(label='opmerkingen?(Gelieve Engels te gebruiken)', blank=True)
    final_payoff = models.FloatField(min=0)