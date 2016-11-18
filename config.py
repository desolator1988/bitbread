# coding: utf8

import os
import uuid


class Config(object):

    DEBUG = False

    SECRET_KEY = 'qwd7qwd23qw2j1wddwdqwd21qwwdn87127-'

    TMP_DIR = '/tmp/'

    # flask mako settings
    MAKO_INPUT_ENCODING = 'utf8'
    MAKO_OUTPUT_ENCODING = 'utf8'
    MAKO_CACHESIZE = 500
    MAKO_TRANSLATE_EXCEPTIONS = False
    MAKO_MODULE_DIRECTORY = TMP_DIR + 'templates{}/'.format(str(uuid.uuid4()).replace('-', ''))
    MAKO_CACHEDIR = TMP_DIR + 'mako/'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass


def load_config():
    """加载配置类"""
    mode = os.environ.get('MODE')
    try:
        if mode == 'PRODUCTION':
            return ProductionConfig
        else:
            return DevelopmentConfig
    except ImportError, e:
        return Config
