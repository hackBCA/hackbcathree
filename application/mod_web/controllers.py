from application import app
from .models import *
import sendgrid
import time
from itsdangerous import URLSafeTimedSerializer

sg = sendgrid.SendGridClient(app.config["SENDGRID_API_KEY"])
ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

def validate_email(entry):
	token = ts.dumps(entry.email, salt = app.config["EMAIL_TOKENIZER_SALT"])
	message = sendgrid.Mail()
	message.add_to(entry.email)
	message.set_from("noreply@hackbca.com")
	message.set_subject("hackBCA III - Mailing List Subscription Confirmation")
	message.set_html("<p></p>")

	message.add_filter("templates", "enable", "1")
	message.add_filter("templates", "template_id", "47174e8a-880e-4bde-978b-6b42caae71af")
	message.add_substitution("token", token)	

	status, msg = sg.send(message)

def confirm_email(token):
	email = ts.loads(token, salt = "email-confirm-key", max_age = 86400)
	entry = MailingListEntry.objects(email = email)[0]
	entry.verified = True
	entry.save()

def add_email(email):
	num_entries = MailingListEntry.objects(email=email).count()
	if num_entries > 0:
		raise Exception("EmailExistsError", "Email already exists in database.")
	new_entry = MailingListEntry(email = email)
	new_entry.save()

	validate_email(new_entry)
