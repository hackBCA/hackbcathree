from mongoengine import *

class MentorRequestTickets(Document):
    hacker_uid = StringField(required = True)
    timestamp = DateTimeField(required = True)
    title = StringField(required = True)
    location = StringField(required = True)
    description = StringField()
    
    tags = ListField(field = StringField())

    mentor_uid = StringField()
    assigned = BooleanField(default = False)
