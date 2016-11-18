mongo:
	mongo anydata --host dds-bp1156dc1fedf0b42.mongodb.rds.aliyuncs.com --port 3717 -u anydata -p anydata123456

redis:
	redis-cli -h 903547a776c8440b.m.cnhza.kvstore.aliyuncs.com -p 6379 -a wbdW8nXb

clear_pyc:
	find . -name '*.pyc' -delete

test: clear_pyc
	env unittest=true py.test ./tests
	env unittest=true py.test ./common --doctest-modules

api_serve:
	gunicorn -c api/gunicorn_config.py api.app:app

dev:
	env dev=true python ./api/app.py
