from flask import *
from . import web_module as mod_web
from . import controllers as controller
from application import cache

@cache.cached()
@mod_web.route("/", methods = ["GET", "POST"])
def index():
	return render_template("web.index.html")

@cache.cached()
@mod_web.route("/sponsors", methods = ["GET"])
def sponsors():
    return mod_web.send_static_file("sponsors.pdf")

@mod_web.route("/sponsors.pdf", methods = ["GET"])
@mod_web.route("/sponsor.pdf", methods = ["GET"])
@mod_web.route("/sponsor", methods = ["GET"])
def foward_sponsors():
    return redirect("/sponsors")

@mod_web.route("/chaperones", methods = ["GET"])
def chaperones():
    return redirect("https://docs.google.com/forms/d/13l1ToVeDeBSEF4OBdHt6gSbYan8xnMFVG6BTRcKrEQw/viewform")

#mod_web.route("/confirm/<token>")
# def confirm_email(token):
# 	controller.confirm_email(token)
# 	return redirect("/?status=confirmed")
