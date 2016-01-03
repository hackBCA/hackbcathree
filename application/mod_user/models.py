from flask.ext.login import LoginManager, UserMixin
from mongoengine import *

application_fields = ["school", "gender", "beginner", "ethnicity", "grade", "num_hackathons", "github_link", "linkedin_link", "site_link", "other_link", "free_response1", "free_response2", "free_response3"]


#Mongo Object
class UserEntry(Document):
	email = StringField(required = True)
	hashed = StringField(required = True)

	firstname = StringField(required = True)
	lastname = StringField(required = True)	

	confirmed = BooleanField(required = False, default = False)

	status = StringField(default = "Not Started")
	# In Progress, Submitted, Accepted, Waitlist, Denied

	type_account = StringField(required = True, default = "Hacker")

	school = StringField()
	gender = StringField()
	beginner = StringField()
	ethnicity = StringField()
	grade = StringField()
	num_hackathons = StringField()
	
	phone = StringField()

	github_link = StringField()
	linkedin_link = StringField()
	site_link = StringField()
	other_link = StringField()

	free_response1 = StringField() #Mentor: Phone Number
	free_response2 = StringField() #Mentor: Skills
	free_response3 = StringField() #Mentor: Workshop		

class User(UserMixin):
	def __init__(self, uid, email, firstname, lastname, type_account, status):

		self.uid = str(uid)
		self.email = email
		self.firstname = firstname
		self.lastname = lastname
		self.type_account = type_account
		self.status = status

	def is_authenticated(self):
		return True

	def get_id(self):
		return self.uid

	def full_name(self):
		return self.firstname + " " + self.lastname
