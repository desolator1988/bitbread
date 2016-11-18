mongo:
	mongo bitbread --host localhost --port 27017 -u bitbread

clear_pyc:
	find . -name '*.pyc' -delete

test: clear_pyc
	env unittest=true py.test ./tests
	env unittest=true py.test ./common --doctest-modules
