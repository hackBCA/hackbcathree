from mongoengine import *

class MailingListEntry(Document):
	email = StringField(max_length = 50, required = True)
	verified = BooleanField(required = False, default = False)

class TeamMemberData(Document):
    team = StringField(required = True)
    first_name = StringField(required = True)
    last_name = StringField(required = True)
    img_slug = StringField(required = True)
    silly_img_slug = StringField(required = True)
    description = StringField(default = "", required = False)
    order = IntField(default = 9001, required = True)

class ScheduleData(Document):
    date = StringField(required = True)
    time = StringField(required = True)
    event = StringField(required = True)
    location = StringField()