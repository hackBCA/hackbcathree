from flask.ext.login import LoginManager, UserMixin
from mongoengine import *

application_fields = ["school", "gender", "beginner", "ethnicity", "grade", "num_hackathons", "github_link", "linkedin_link", "site_link", "other_link", "resp1", "resp2", "resp3"]

#Mongo Object
class UserEntry(Document):
	email = StringField(required = True)
	hashed = StringField(required = True)

	firstname = StringField(required = True)
	lastname = StringField(required = True)	

	verified = BooleanField(required = False, default = False)

	hacker = BooleanField(required = True, default = True)

	school = StringField()
	gender = StringField()
	beginner = StringField()
	ethnicity = StringField()
	grade = StringField()
	num_hackathons = StringField()
	
	github_link = StringField()
	linkedin_link = StringField()
	site_link = StringField()
	other_link = StringField()

	resp1 = StringField()
	resp2 = StringField()
	resp3 = StringField()	


class User(UserMixin):
	def __init__(self, uid, email, firstname, lastname, hacker):
		self.uid = str(uid)
		self.email = email
		self.firstname = firstname
		self.lastname = lastname
		self.hacker = hacker

	def is_authenticated(self):
	    return True

	def get_id(self):
	    return self.uid
