from .models import *

def add_email(email):
	new_entry = MailingListEntry(email = email)
	new_entry.save()