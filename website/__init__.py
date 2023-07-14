from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
import random
import sqlite3
from oauthlib.oauth2 import WebApplicationClient


GOOGLE_CLIENT_ID = os.environ.get("113087941687-umil4kt4oulh9p35h9uu1r9ssvlqlbl8.apps.googleusercontent.com", None)
GOOGLE_CLIENT_SECRET = os.environ.get("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", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)
DB = SQLAlchemy()
DB_NAME = "site.db"
def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = '**CHANGE ME IMMEDIATELY**'
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	DB.init_app(app)
	from .templates.views import views
	from .templates.auth import auth

	app.register_blueprint(views, url_prefix="/")
	app.register_blueprint(auth, url_prefix="/")

	from .templates.models import AuthenticatedUser
	if not os.path.exists('website/' + DB_NAME):
		with app.app_context():
			DB.create_all()
			print('Database created')	

	
	login_manager = LoginManager()
	login_manager.init_app(app)
	login_manager.login_view = 'auth.login'


	@login_manager.user_loader
	def load_user(id):
		print(f"user loaded {id}")
		return AuthenticatedUser.query.filter_by(id=id).first()
	return app


