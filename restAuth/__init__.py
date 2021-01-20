from flask import Flask
from config import DevelopmentConfig


def create_app(config_file):

	app = Flask(__name__,instance_relative_config=True)
	app.config.from_object('config.DevelopmentConfig')

	return app