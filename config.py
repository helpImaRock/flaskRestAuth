import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

	DEBUG=False
	TESTING=False


class ProductionConfig(Config):
	pass

class DevelopmentConfig(Config):
	DEBUG=True
	EXPLAIN_TEMPLATE_LOADING=True
	TESTING=True

class TestingConfig(Config):
	pass