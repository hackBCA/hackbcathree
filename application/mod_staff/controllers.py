from application import CONFIG, app
from .models import *
from flask.ext.login import login_user
import bcrypt

staff_login_manager = LoginManager()

staff_login_manager.init_app(app)

@staff_login_manager.user_loader
def load_user(user_id):	
	user_entries = StaffEntry.objects(id = user_id)
	if user_entries.count() != 1:
		return None
	currUser = user_entries[0]
	user = User(currUser.id, currUser.username, currUser.firstname, currUser.lastname, currUser.email) 
	return user

def verify_user(username, password):
	user_entries = StaffEntry.objects(username = username)
	
	if user_entries.count() != 1:
		raise Exception("UserDoesNotExistError", "Invalid Username")
	currUser = user_entries[0]	
	hashed = currUser.hashed		

	if bcrypt.hashpw(password.encode("utf-8"), hashed.encode("utf-8")) == hashed.encode("utf-8"):
		return load_user(currUser.id)
	else:
		return None

def login(username, password):
	user = verify_user(username, password)
	if user != None:
		login_user(user)

def logout(_):
		logout_user()

def add_user(username, password, first, last, email):
	num_entries = StaffEntry.objects(username=username).count()
	if num_entries > 0:
		raise Exception("UserExistsError", "Username already exists in database.")

	hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
	
	new_entry = StaffEntry(username = username, hashed = hashed, firstname = first, lastname = last, email = email)
	new_entry.save()
