from flask import *
from . import web_module as mod_web
from . import controllers
from application import cache

@cache.cached()
@mod_web.route("/", methods = ["GET", "POST"])
def index():
	return render_template("web.index.html")

@cache.cached()
@mod_web.route("/rules", methods = ["GET", "POST"])
def rules():
    return render_template("web.rules.html")

@mod_web.route("/team", methods = ["GET"])
def team():
    board = controllers.get_team_members_by_team(["board"])[0]
    team_list = ["finance", "logistics", "outreach", "promotions", "sponsors", "tech"]
    teams = controllers.get_team_members_by_team(team_list)
    return render_template("web.team.html", board = board, teams = teams)

@cache.cached()
@mod_web.route("/sponsors", methods = ["GET"])
def sponsors():
    return mod_web.send_static_file("sponsors.pdf")

@mod_web.route("/sponsors.pdf", methods = ["GET"])
@mod_web.route("/sponsor.pdf", methods = ["GET"])
@mod_web.route("/sponsor", methods = ["GET"])
def foward_sponsors():
    return redirect("/sponsors")

@mod_web.route("/privacy", methods = ["GET"])
def privacy():
    return mod_web.send_static_file("privacystatement.pdf")

@mod_web.route("/privacy.pdf", methods = ["GET"])
@mod_web.route("/privacystatement.pdf", methods = ["GET"])
def forward_privacy():
    return redirect("/privacy")

@mod_web.route("/chaperones", methods = ["GET"])
def chaperones():
    return redirect("https://docs.google.com/forms/d/13l1ToVeDeBSEF4OBdHt6gSbYan8xnMFVG6BTRcKrEQw/viewform")

@mod_web.route("/enterschedule")
def schedule():
    return controllers.get_schedule()
#     data = [
#         {
#             "date": "Sunday, April 03", 
#             "time": 
#             "2:00 AM", 
#             "event": "Pizza",
#             "location": "Lower Cafeteria"
#         },
#         {
#             "date": "Sunday, April 03", 
#             "time": 
#             "7:30 AM", 
#             "event": "Breakfast",
#             "location": "Lower Cafeteria"
#         },
#         {
#             "date": "Sunday, April 03", 
#             "time": 
#             "11:30 AM", 
#             "event": "Lunch",
#             "location": "Lower Cafeteria"
#         },
#         {
#             "date": "Sunday, April 03", 
#             "time": 
#             "12:30 PM", 
#             "event": "Hacks Must be Submitted",
#             "location": ""
#         },
#         {
#             "date": "Sunday, April 03", 
#             "time": 
#             "1:00 PM", 
#             "event": "Demos Begin",
#             "location": "Gym, Upper Cafeteria"
#         },
#         {
#             "date": "Sunday, April 03", 
#             "time": 
#             "3:00 PM", 
#             "event": "Demos End, Closing Ceremony Begins",
#             "location": "Auditorium"
#         },
#         {
#             "date": "Sunday, April 03", 
#             "time": 
#             "4:00 PM", 
#             "event": "Hackathon Ends",
#             "location":""
#         },
#         {
#             "date": "Saturday, April 02", 
#             "time": 
#             "1:30 PM", 
#             "event": "Registration Begins",
#             "location": "Auditorium Foyer"
#         },
#         {
#             "date": "Saturday, April 02", 
#             "time": 
#             "3:00 PM", 
#             "event": "Opening Ceremony Begins",
#             "location": "Auditorium"
#         },
#         {
#             "date": "Saturday, April 02", 
#             "time": 
#             "4:30 PM", 
#             "event": "Opening Ceremony Ends, Hacking Begins",
#             "location": "Gym, Lower Cafeteria, Upper Cafeteria, Basement Hallway"
#         },
#         {
#             "date": "Saturday, April 02", 
#             "time": 
#             "6:30 PM", 
#             "event": "Dinner",
#             "location": "Lower Cafeteria"
#         },
#         {
#             "date": "Saturday, April 02", 
#             "time": 
#             "11:00 PM", 
#             "event": "Snack",
#             "location": "Lower Cafeteria"
#         }
#     ]
#     controllers.schedule(data)
#     return "hi"

#mod_web.route("/confirm/<token>")
# def confirm_email(token):
# 	controllers.confirm_email(token)
# 	return redirect("/?status=confirmed")
