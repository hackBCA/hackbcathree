from mongoengine import *

class MailingListEntry(Document):
	email = StringField(max_length = 50, required=True)