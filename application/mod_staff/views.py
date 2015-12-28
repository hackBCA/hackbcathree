from flask import render_template, redirect, request
from flask.ext.login import login_required
from . import staff_module as mod_staff
from . import controllers as controller

@mod_staff.route("/")
def index():
	return render_template("staff_login.html")

@mod_staff.route("/login", methods = ["GET", "POST"])
def login():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		controller.login(username, password)
		return redirect("staff/index")
		# return render_template("staff_index.html", username=username)
	return render_template("staff_login.html")

@mod_staff.route("/index", methods = ["GET", "POST"])
@login_required
def home():
	return render_template("staff_index.html")

@mod_staff.route("/logout", methods = ["GET", "POST"])
def logout():
	if request.method == "POST":
		controller.logout()
		return redirect("staff/login")
	return render_template("staff_logout.html")

@mod_staff.route("/register", methods = ["GET", "POST"])
@login_required
def register():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		first_name = request.form["first_name"]
		last_name = request.form["last_name"]
		email = request.form["email_address"]
		controller.add_user(username, password, first_name, last_name, email)
		return redirect("staff/index")

	return render_template("staff_register.html")

@mod_staff.route("/secret")
@login_required
def secret():
	return render_template("staff_secret.html")
