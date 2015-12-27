from flask import render_template, redirect
from flask.ext.login import login_required
from . import staff_module as mod_staff
from . import controllers as controller

@mod_staff.route("/")
def index():
	return render_template("login.html")
	
@mod_staff.route("/login")
def login():
  return render_template("login.html")

@mod_staff.route("/secret")
@login_required
def secret():
	return render_template("secret.html")