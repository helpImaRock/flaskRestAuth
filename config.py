import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

	DEBUG=False
	TESTING=False

'''
	Environment configs
'''

class ProductionConfig(Config):
	pass

class DevelopmentConfig(Config):
	DEBUG=True
	EXPLAIN_TEMPLATE_LOADING=True
	TESTING=True

class TestingConfig(Config):
	pass

'''
	Database configs

'''
class SQLiteDevelopmentConfig(DevelopmentConfig):
	SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
	SQLALCHEMY_TRACK_MODIFICATIONS=False