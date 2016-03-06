from application import CONFIG
from .models import *
import sendgrid
import time
from itsdangerous import URLSafeTimedSerializer
from itertools import groupby

sg = sendgrid.SendGridClient(CONFIG["SENDGRID_API_KEY"])
ts = URLSafeTimedSerializer(CONFIG["SECRET_KEY"])

def validate_email(entry):
    token = ts.dumps(entry.email, salt = CONFIG["EMAIL_TOKENIZER_SALT"])
    message = sendgrid.Mail()
    message.add_to(entry.email)
    message.set_from("contact@hackbca.com")
    message.set_subject("hackBCA III - Mailing List Subscription Confirmation")
    message.set_html("<p></p>")

    message.add_filter("templates", "enable", "1")
    message.add_filter("templates", "template_id", CONFIG["SENDGRID_MAILING_LIST_CONFIRM_TEMPLATE"])
    message.add_substitution("token", token)    

    status, msg = sg.send(message)

def confirm_email(token):
    email = ts.loads(token, salt = CONFIG["EMAIL_TOKENIZER_SALT"], max_age = 86400)
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

def ugh():
    entries = TeamMemberData.objects()
    for entry in entries:
        silly = entry.silly_img_slug[:-4]
        if "profile.png" not in entry.silly_img_slug:
            entry.silly_img_slug = silly + "_silly.jpg"
            entry.save()


def get_team_members_by_team(teams):
    all_teams = []
    for team in teams:
        members = TeamMemberData.objects(team = team)
        packaged = {
            "team": team,
            "members": [
                {
                    "first_name": member.first_name,
                    "last_name": member.last_name,
                    "img_slug": member.img_slug,
                    "silly_img_slug": member.silly_img_slug,
                    "description": member.description,
                    "order": member.order
                } for member in members
            ]
        }
        packaged["members"] = sorted(
                                packaged["members"], 
                                key = lambda k: (
                                    k["order"],
                                    k["description"], 
                                    k["last_name"], 
                                    k["first_name"])
                                )
        all_teams.append(packaged)
    return all_teams


