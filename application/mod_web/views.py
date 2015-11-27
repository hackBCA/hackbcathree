from flask import render_template, redirect
from . import web_module as mod_web
from .controllers import *

@mod_web.route("/")
def index():
    return render_template("index.html")

@mod_web.route("/sponsors",methods=["GET"])
def sponsors():
    return mod_web.send_static_file("sponsors.pdf")

@mod_web.route("/sponsors.pdf",methods=["GET"])
def foward_sponsors():
    return redirect("/sponsors")