import os

DEBUG = False
TESTING = False

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(PROJECT_ROOT, 'graphql.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = True


LOGGING_CONFIG = {
    'version': 1,
    'root': {
        'level': 'NOTSET',
        'handlers': ['default'],
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s: %(levelname)s / %(name)s] %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'main_api': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}
