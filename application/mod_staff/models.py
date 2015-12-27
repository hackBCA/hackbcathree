from flask.ext.login import LoginManager, UserMixin
from mongoengine import *

#Mongo Object
class StaffEntry(Document):
	username = StringField(required = True)
	firstname = StringField(required = True)
	lastname = StringField(required = True)	
	email = StringField(required = True)

	hashed = StringField(required = True)
	def __repr__(self):
		return ', '.join([self.username, self.firstname, self.lastname, self.email])

class User(UserMixin):
	def __init__(self, uid, username, firstname, lastname, email):
		self.uid = str(uid)
		self.username = username
		self.firstname = firstname
		self.lastname = lastname
		self.email = email

	def is_authenticated(self):
	    return True

	def get_id(self):
	    return self.uid
	