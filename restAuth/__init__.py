from flask import Flask
from config import DevelopmentConfig
from flask_marshmallow import Marshmallow
from .auth import auth as authbp

ma = Marshmallow()

def create_app(config_file):

	app = Flask(__name__,instance_relative_config=True)
	app.config.from_object('config.DevelopmentConfig')

	## extensions
	ma.init_app(app)

	## blueprints
	app.register_blueprint(authbp,url_prefix='/account')

	return app