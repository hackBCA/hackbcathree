from .models import *

def add_email(email):
	print('Test')
	new_entry = MailingListEntry(email = 'test@test.com')
	new_entry.save()