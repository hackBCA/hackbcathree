from application import CONFIG, app
from .models import *
from flask.ext.login import login_user, logout_user
import bcrypt
import re
import sendgrid
import time
from itsdangerous import URLSafeTimedSerializer

login_manager = LoginManager()
login_manager.init_app(app)

sg = sendgrid.SendGridClient(CONFIG["SENDGRID_API_KEY"])
ts = URLSafeTimedSerializer(CONFIG["SECRET_KEY"])

@login_manager.user_loader
def load_user(user_id):	
	user_entries = UserEntry.objects(id = user_id)
	if user_entries.count() != 1:
		return None
	currUser = user_entries[0]
	user = User(currUser.id, currUser.email, currUser.firstname, currUser.lastname) 
	return user

def get_user(email):
	entries = UserEntry.objects(email = email)

	if entries.count() == 1:
		return entries[0]
	return None

def verify_user(email, password):
	currUser = get_user(email)

	if currUser is None:
		return None

	hashed = currUser.hashed		

	if bcrypt.hashpw(password.encode("utf-8"), hashed.encode("utf-8")) == hashed.encode("utf-8"):
		return load_user(currUser.id)
	else:
		return None

def login(email, password):
	user = verify_user(email, password)

	if user != None:
		login_user(user)
	else:
		raise Exception("AuthenticationError", "Invalid credentials.")

def logout():
	logout_user()

def add_user(email, firstname, lastname, password):
	existingUser = get_user(email)
	if existingUser is not None:
		raise Exception("UserExistsError", "Username already exists in database.")
	
	hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
	new_entry = UserEntry(email = email, hashed = hashed, firstname = firstname, lastname = lastname)
	new_entry.save()
	
	validate_email(new_entry)

def tokenize_email(email):
	return ts.dumps(email, salt = CONFIG["EMAIL_TOKENIZER_SALT"])
def detokenize_email(token):
	return ts.loads(token, salt = CONFIG["EMAIL_TOKENIZER_SALT"], max_age = 86400)

def send_recovery_email(email):
	user = get_user(email)

	if user is None:
		raise Exception("UserDoesNotExistError", "Account with given email does not exist.")

	token = tokenize_email(email)
	message = sendgrid.Mail()
	message.add_to(email)
	message.set_from("noreply@hackbca.com")
	message.set_subject("hackBCA III - Account Recovery")
	message.set_html("<p></p>")

	message.add_filter("templates", "enable", "1")
	message.add_filter("templates", "template_id", CONFIG["SENDGRID_ACCOUNT_RECOVERY_TEMPLATE"])
	message.add_substitution("token", token)	

	status, msg = sg.send(message)

def change_password(email, password):
	account = get_user(email)
	hashed = str(bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()))[2:-1]
	account.hashed = hashed
	account.save()

def validate_email(entry):
	token = tokenize_email(entry.email)
	message = sendgrid.Mail()
	message.add_to(entry.email)
	message.set_from("noreply@hackbca.com")
	message.set_subject("hackBCA III - Account Creation Confirmation")
	message.set_html("<p></p>")

	message.add_filter("templates", "enable", "1")
	message.add_filter("templates", "template_id", CONFIG["SENDGRID_ACCOUNT_CONFIRM_TEMPLATE"])
	message.add_substitution("token", token)	

	status, msg = sg.send(message)

def confirm_email(token):
	email = detokenize_email(token)
	entry = UserEntry.objects(email = email)[0]
	entry.verified = True
	entry.save()