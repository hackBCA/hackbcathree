from application import CONFIG, app
from .models import *
from flask.ext.login import login_user
import bcrypt
import re

user_login_manager = LoginManager()

user_login_manager.init_app(app)

@user_login_manager.user_loader
def load_user(user_id):	
	user_entries = UserEntry.objects(id = user_id)
	if user_entries.count() != 1:
		return None
	currUser = user_entries[0]
	user = User(currUser.id, currUser.username, currUser.firstname, currUser.lastname, currUser.email) 
	return user

def verify_user(email, password):
	user_entries = UserEntry.objects(email = email)
	
	if user_entries.count() != 1:
		raise Exception("UserDoesNotExistError", "Invalid Username")
	currUser = user_entries[0]	
	hashed = currUser.hashed		

	if bcrypt.hashpw(password.encode("utf-8"), hashed.encode("utf-8")) == hashed.encode("utf-8"):
		return load_user(currUser.id)
	else:
		return None

def login(email, password):
	user = verify_user(email, password)
	if user != None:
		login_user(user)

def logout(_):
		logout_user()

def add_user(email, firstname, lastname, password):
	num_entries = UserEntry.objects(email = email).count()
	if num_entries > 0:
		raise Exception("UserExistsError", "Username already exists in database.")

	hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
	
	new_entry = UserEntry(email = email, hashed = hashed, firstname = firstname, lastname = lastname)
	new_entry.save()
	validate_email(new_entry)

import sendgrid
import time
from itsdangerous import URLSafeTimedSerializer

sg = sendgrid.SendGridClient(CONFIG["SENDGRID_API_KEY"])
ts = URLSafeTimedSerializer(CONFIG["SECRET_KEY"])

def validate_email(entry):
	print(entry.email, CONFIG["SENDGRID_ACCOUNT_CONFIRM_TEMPLATE"])

	token = ts.dumps(entry.email, salt = CONFIG["EMAIL_TOKENIZER_SALT"])
	message = sendgrid.Mail()
	message.add_to(entry.email)
	message.set_from("noreply@hackbca.com")
	message.set_subject("hackBCA III - Account Creation Confirmation")
	message.set_html("<p></p>")

	print("Here")

	message.add_filter("templates", "enable", "1")
	message.add_filter("templates", "template_id", CONFIG["SENDGRID_ACCOUNT_CONFIRM_TEMPLATE"])
	message.add_substitution("token", token)	

	status, msg = sg.send(message)

def confirm_email(token):
	email = ts.loads(token, salt = CONFIG["EMAIL_TOKENIZER_SALT"], max_age = 86400)
	entry = UserEntry.objects(email = email)[0]
	entry.verified = True
	entry.save()