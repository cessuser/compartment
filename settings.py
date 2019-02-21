from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'compartment_trt1',
        'display_name': "compartment_trt1",
        'num_demo_participants': 1,
        'treatment': 1,
        'app_sequence': ['number_add1', 'word_search', 'Vignette'],
    },
    {
        'name': 'compartment_trt2',
        'display_name': "compartment_trt2",
        'num_demo_participants': 1,
        'treatment': 2,
        'app_sequence': ['number_add1', 'word_search', 'Vignette'],
    },
    {
        'name': 'compartment_trt3',
        'display_name': "compartment_trt3",
        'num_demo_participants': 1,
        'treatment': 3,
        'app_sequence': ['number_add1', 'word_search', 'Vignette'],
    },
    {
        'name': 'compartment_trt4',
        'display_name': "compartment_trt4",
        'num_demo_participants': 1,
        'treatment': 4,
        'app_sequence': ['number_add1', 'word_search', 'Vignette'],
    },

]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


ROOMS = [
    {
        'name': 'test',
        'display_name': 'test_US',
    },
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'rv^bfmedsz3=rgvv%f+4if(!cm-y7jx&duzkqy3o=6&j4p16yy'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
