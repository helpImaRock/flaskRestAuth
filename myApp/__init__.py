from flask import Flask
from .auth import auth as authbp


def create_app(config_file):

	app = Flask(__name__,instance_relative_config=True)
	app.config.from_object('config.SQLiteDevelopmentConfig')

	with app.app_context():
		from .models import db
		db.init_app(app)
	
	### blueprints
	app.register_blueprint(authbp)

	return app