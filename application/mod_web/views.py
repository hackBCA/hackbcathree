from flask import render_template, redirect
from . import web_module as web

@web.route("/")
def index():
    return render_template("index.html")

@web.route("/sponsors",methods=["GET"])
def sponsors():
    return web.send_static_file("sponsors.pdf")

@web.route("/sponsors.pdf",methods=["GET"])
def foward_sponsors():
    return redirect("/sponsors")