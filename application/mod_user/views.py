from flask import render_template, redirect, request, flash
from flask.ext.login import login_required
from . import user_module as mod_user
from . import controllers as controller
from .forms import RegistrationForm, LoginForm, ApplicationForm
from application import CONFIG

@mod_user.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm(request.form)
	if request.method == "POST" and form.validate():
		print("Hello there!")
		try:
			controller.login(request.form["email"], request.form["password"])

		except Exception as e:
			print(CONFIG["DEBUG"])
			exceptionType = e.args[0]
			if exceptionType == "AuthenticationError":
				print(exceptionType)
				flash("Invalid email and/or password.", "error")
			else:
				if(CONFIG["DEBUG"]):
					raise e
				else:
					flash("Something went wrong.", "error")
	return render_template("user_login.html", form = form)

@mod_user.route("/account")
@login_required
def account():
	return render_template("user_account.html")

@mod_user.route("/register", methods=["GET", "POST"])
def register():
	form = RegistrationForm(request.form)
	if request.method == "POST" and form.validate():
		try:
			controller.add_user(request.form["email"], request.form["first_name"], request.form["last_name"], request.form["password"])
			flash("Almost there! Check your inbox for a verification email to confirm your account.", "success")
		except Exception as e:
			exceptionType = e.args[0]
			if exceptionType == "UserExistsError":
				flash("A user with that email already exists.", "error")
			else:
				if CONFIG["DEBUG"]:
					raise e
				else:
					flash("Something went wrong.", "error")
	return render_template("user_register.html", form = form)

@mod_user.route("/application", methods = ["GET", "POST"])
def application():
	form = ApplicationForm(request.form)
	if request.method == "POST" and form.validate():
		pass #TO-DO when application controller is done
	return render_template("user_application.html", form = form)

@mod_user.route("/confirm/<token>")
def confirm_email(token):
	controller.confirm_email(token)
	return redirect("/?status=confirmed");
