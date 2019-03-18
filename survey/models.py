from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

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
    age = models.IntegerField(min=18, max=100, label="1.What is your age?")
    gender = models.StringField(choices=['Female', 'Male'], label="What is your gender?", widget=widgets.RadioSelect)
    gender_other = models.StringField(label="other(Please specify) ", blank=True)
    student = models.StringField(
        choices=["Full time", "Part time (less than the normal full time course load)", "Non-student"],
        label="3.What is your student status?")
    edu_level = models.StringField(
        label="4.What is the highest level of study that you have completed? (Use your current year in school if you are a student.)",
        choices=['High school or lower', 'Undergraduate 1st year', 'Undergraduate 2nd year',
                 'Undergraduate 3rd year', 'Undergraduate 4th year', 'Graduate 1st year', 'Graduate 2nd year',
                 'Graduate 3 or more years'], widget=widgets.RadioSelect)
    major = models.StringField(
        label="5.Which of the following best describes your current major course of study? (Check more than one option if you are a double major or if your undergraduate and graduate majors differ. For non-students, use the major for the highest year of school completed.)",
        choices=['No Major or Pre-College',
                 'Arts/Humanities/Education',
                 'Business/Management (including MBA)',
                 'Economics',
                 'Politics',
                 'Psychology',
                 'Other Social Sciences',
                 'Law School (but not pre-law)',
                 'Medical/Nursing (but not pre-med)',
                 'Math/Engineering/Computer Science/Science'],
        widget=widgets.RadioSelect)
    major_other = models.StringField(label="other(Please specify)", blank=True)
    math_course = models.IntegerField(label="6.How many college-level mathematics courses have you taken")
    econ_course = models.IntegerField(label="7.How many college-level economics courses have you taken?")

    final_payoff = models.FloatField(min=0)