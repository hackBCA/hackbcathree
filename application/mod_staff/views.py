from flask import render_template, redirect
from . import staff_module as mod_staff

@mod_staff.route("/")
def index():
	return render_template("login.html")
	
@mod_staff.route("/login")
def login():
  return render_template("login.html")

