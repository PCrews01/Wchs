from website import DB
from flask_login import UserMixin

class Users(DB.Model, UserMixin):
	id = DB.Column(DB.Integer, primary_key=True)
	name = DB.Column(DB.String(50))
	email = DB.Column(DB.String(50), unique=True)

class Academics(DB.Model):
	id = DB.Column(DB.Integer, primary_key=True)
	title = DB.Column(DB.String, unique=True)
	staff = DB.Column(DB.Integer)
	students = DB.Column(DB.Integer)
	blurb = DB.Column(DB.String)

class Sport(DB.Model):
	id = DB.Column(DB.Integer, primary_key=True)
	sport = DB.Column(DB.String, unique=True)
	losses = DB.Column(DB.Integer)
	wins = DB.Column(DB.Integer)
	ties = DB.Column(DB.Integer)
	coach = DB.Column(DB.String)
	championships = DB.Column(DB.String)
	winning_years = DB.Column(DB.String)
	
class AuthenticatedUser(DB.Model, UserMixin):
	id = DB.Column(DB.Integer, primary_key=True)
	unique_id = DB.Column(DB.String, unique=True)
	first_name = DB.Column(DB.String)
	last_name = DB.Column(DB.String)
	email = DB.Column(DB.String)
	profile_picture = DB.Column(DB.String, nullable=True)
	is_active = DB.Column(DB.Boolean, default=False)
	picture = DB.Column(DB.String)
	verified = DB.Column(DB.Boolean)

class Article(DB.Model):
	id = DB.Column(DB.Integer, primary_key=True)
	title = DB.Column(DB.String, unique=True)
	story = DB.Column(DB.String, nullable=False)
	headline = DB.Column(DB.String)
	date = DB.Column(DB.String)
	author = DB.Column(DB.String, nullable=False)
	image = DB.Column(DB.String) #Comma separated string
	category = DB.Column(DB.String)
	tags = DB.Column(DB.String) #Comma separated string
	lead_story = DB.Column(DB.Boolean, default=False)
