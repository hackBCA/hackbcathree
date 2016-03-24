from flask.ext.login import LoginManager, UserMixin
from mongoengine import *

application_fields = ["school", "gender", "beginner", "ethnicity", "grade", "num_hackathons", "phone", "github_link", "linkedin_link", "site_link", "other_link", "free_response1", "free_response2", "free_response3", "mlh_terms"]

#Mongo Object
class UserEntry(Document):
	email = StringField(required = True)
	hashed = StringField(required = True)

	firstname = StringField(required = True)
	lastname = StringField(required = True)

	confirmed = BooleanField(required = False, default = False)

	status = StringField(default = "Not Started")
	# In Progress, Submitted, Accepted, Waitlist

	type_account = StringField(required = True, default = "hacker")

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

	intended_major = StringField()
	other_intended_major = StringField()

	reduced_lunch = StringField()

	hear_about_us = StringField()
	other_hear_about_us = StringField()

	free_response1 = StringField() #Mentor: Phone Number
	free_response2 = StringField() #Mentor: Skills
	free_response3 = StringField() #Mentor: Workshop

	mlh_terms = StringField()

	review1 = IntField()
	reviewer1 = StringField()
	review2 = IntField()
	reviewer2 = StringField()
	review3 = IntField()
	reviewer3 = StringField()

	decision = StringField()
	accepted_time = IntField()
	attending = StringField()
	rsvp = BooleanField(default = False) #Has the user submitted their rsvp form?

	address = StringField()
	phone = StringField()
	t_shirt_size = StringField()

	emergency_contact_name1 = StringField()
	emergency_contact_phone1 = StringField()
	emergency_contact_relation1 = StringField()

	emergency_contact_name2 = StringField()
	emergency_contact_phone2 = StringField()
	emergency_contact_relation2 = StringField()

	food_allergies = StringField()
	medical_information = StringField()
	hackbca_rules = StringField()

	checked_in = BooleanField(default = False)
	check_in_log = ListField()

	waiver = BooleanField(default = False)

	smsblast_optin = BooleanField(default = False)

class User(UserMixin):
	def __init__(self, uid, email, firstname, lastname, type_account, status, decision, attending, checked_in):

		self.uid = str(uid)
		self.email = email
		self.firstname = firstname
		self.lastname = lastname
		self.type_account = type_account
		self.status = status
		self.decision = decision
		self.attending = attending
		self.checked_in = checked_in

	def is_authenticated(self):
		return True

	def get_id(self):
		return self.uid

	def full_name(self):
		return self.firstname + " " + self.lastname
