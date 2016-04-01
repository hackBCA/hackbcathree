from flask import *
from . import web_module as mod_web
from . import controllers
from application import cache

@cache.cached()
@mod_web.route("/", methods = ["GET", "POST"])
def index():
    schedule = controllers.get_schedule()
    return render_template("web.index.html", schedule = schedule)

@mod_web.route("/schedule")
def forward_schedule():
    return redirect("/#schedule")

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

@cache.cached()
@mod_web.route("/waiver", methods = ["GET"])
def waiver():
    return mod_web.send_static_file("waiver.pdf")

@mod_web.route("/waiver.pdf", methods = ["GET"])
def foward_waiver():
    return redirect("/waiver")

@mod_web.route("/hardware", methods = ["GET"])
def hardware():
    return mod_web.send_static_file("hardware.pdf")

@mod_web.route("/workshops", methods = ["GET"])
def workshops():
    return mod_web.send_static_file("workshops.pdf")

@mod_web.route("/workshop", methods = ["GET"])
def workshop():
    return redirect("workshops")

@mod_web.route("/checklist", methods = ["GET"])
def checklist():
    return mod_web.send_static_file("checklist.pdf")

@cache.cached()
@mod_web.route("/map", methods = ["GET"])
def map():
    return mod_web.send_static_file("map.jpg")

@mod_web.route("/map.jpeg", methods = ["GET"])
@mod_web.route("/map.jpg", methods = ["GET"])
def foward_map():
    return redirect("/map")

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

#For mailing list
#mod_web.route("/confirm/<token>")
# def confirm_email(token):
# 	controllers.confirm_email(token)
# 	return redirect("/?status=confirmed")
