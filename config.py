

class Config(object):

	DEBUG=False
	TESTING=False


class ProductionConfig(Config):
	pass

class DevelopmentConfig(Config):
	DEBUG=True
	EXPLAIN_TEMPLATE_LOADING=True

class TestingConfig(Config):
	TESTING=True