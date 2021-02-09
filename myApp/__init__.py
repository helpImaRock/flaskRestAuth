from flask import Flask
from .auth import auth as authbp
from werkzeug.exceptions import HTTPException

def create_app(config_file):

	app = Flask(__name__,instance_relative_config=True)
	app.config.from_object('config.SQLiteDevelopmentConfig')

	with app.app_context():
		from .models import db
		
		## configuration
		
		# check has_static_folder setting

		db.init_app(app)
		
		### blueprints
	
		app.register_blueprint(authbp)
		from .errors import handle_exception
		app.register_error_handler(HTTPException, handle_exception)
	

	return app