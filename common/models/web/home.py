# coding: utf8

from mongoengine import *


class TestBitbread(Document):

    kind = 'K_TEST_BREAD'
    kind_cn = u'测试表'
    source_cn = u'测试表'

    id = StringField(primary_key=True)
    name = StringField()

    meta = {
        'collection': 'test_bitbread',
        'indexes': ['name'],
        'strict': False,
    }
