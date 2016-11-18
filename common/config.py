import os

PYTHON = '/srv/virtualenvs/bitbread/bin/python'

CRON_USER = 'www-data'


MONGO_URL = 'mongodb://anydata:anydata123456@dds-bp1156dc1fedf0b41.mongodb.rds.aliyuncs.com:3717,dds-bp1156dc1fedf0b41.mongodb.rds.aliyuncs.com:3717'
MONGO_DB = 'bitbread'
MONGO_REP_SET = 'mgset-1036203'

MONGO_CONFIG_STAGING = dict(
    db='bitbread',
    host='localhost',
    port=27017,
    username=None,
    passwd=None,
)

ES_HOST = '106.14.31.54 '
ES_PORT = 8848


ROOT_DIR = os.path.abspath(__file__).split('bitbread')[0] + 'bitbread/'
TMP_DIR = '/tmp/'
DATA_DIR = '/data/'


OSS_HOST = 'oss-cn-hangzhou.aliyuncs.com'
OSS_ACCESS_KEY_ID = 'unTa13H01qeyV6BV'
OSS_ACCESS_KEY_SECRET = '2NWjcPU3jk8GWY9L3emyVVZoZcGUrU'


OCS_HOST = 'f7cfe8921f954b52.m.cnhzaliqshpub001.ocs.aliyuncs.com'
OCS_PORT = 11211
OCS_USER = 'f7cfe8921f954b52'
OCS_PWD = 'qwd8nqKjqwd'

IMAGE_BASE = 'http://dataimg.fellowplus.com/'

SLACK_API_TOKEN = 'xoxp-17670964721-17668736707-18554626580-67ce2a0ee9'

APP_SECRET_KEY = '0f7307ff24064a3aa81eed7b2dac70ac'
APP_SECURITY_PASSWORD_SALT = '347caf6c03654e1194108e806a28c5a7'


# import platform
# if 'Darwin' in platform.uname():
#     try:
#         from .local_config import *  # NOQA
#     except:
#         pass

unittest_env = bool(os.environ.get('unittest'))
