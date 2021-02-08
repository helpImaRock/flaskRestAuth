from flask import Flask
from config import DevelopmentConfig
from .auth import auth as authbp


def create_app(config_file):

	app = Flask(__name__,instance_relative_config=True)
	app.config.from_object('config.DevelopmentConfig')

	with app.app_context():
		pass
	
	### blueprints
	app.register_blueprint(authbp)

	return app