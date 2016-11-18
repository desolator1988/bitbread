from logging import config as logging_config

LOGGING_SETTINGS = {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'loggers': {
            'hermes': {
                'handlers': ['console'],
                'propagate': False,
                'level': 'DEBUG',
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'general',
            },
        },
        'formatters': {
            'general': {
                'format': '%(asctime)s %(levelname)-6s [%(name)s][%(process)d]'
                          ' %(message)s'
            },
            'detail': {
                'format': '%(asctime)s %(levelname)-6s [%(name)s][%(process)d]'
                          '[%(pathname)s: %(lineno)d] '
                          '%(message)s',
            },
        }
    }

logging_config.dictConfig(LOGGING_SETTINGS)


from elasticsearch_dsl.connections import connections
from config import ES_HOST
es = connections.create_connection(hosts=[ES_HOST])
