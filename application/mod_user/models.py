from flask.ext.login import LoginManager, UserMixin
from mongoengine import *

#Mongo Object
class UserEntry(Document):
	firstname = StringField(required = True)
	lastname = StringField(required = True)	
	email = StringField(required = True)

	verified = BooleanField(required = False, default = False)

	hashed = StringField(required = True)
	def __repr__(self):
		return ', '.join([self.firstname, self.lastname, self.email])

class User(UserMixin):
	def __init__(self, uid, email, firstname, lastname):
		self.uid = str(uid)
		self.email = email
		self.firstname = firstname
		self.lastname = lastname

	def is_authenticated(self):
	    return True

	def get_id(self):
	    return self.uid