# coding: utf8
from gevent import monkey
monkey.patch_all(subprocess=True)
from mongoengine import connect
from common.config import (
    unittest_env,
    MONGO_CONFIG_STAGING as staging_config,
)


if unittest_env:
    from mongoengine import connection
    from mongomock.mongo_client import MongoClient
    connection.MongoClient = MongoClient
    connect('bitbread')
else:
    import platform
    if 'Darwin' in platform.uname():
        from common.local_config import MONGO_CONFIG
        print 'in Darwin......'
        print connect(MONGO_CONFIG['db'], host=MONGO_CONFIG['host'], port=MONGO_CONFIG['port'])
    else:
        connect('bitbread', host='localhost', port=27017)
