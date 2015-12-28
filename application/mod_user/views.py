from flask import render_template, redirect, request, flash
from flask.ext.login import login_required
from . import user_module as mod_user
from . import controllers as controller
from .forms import RegistrationForm, LoginForm, EmailForm, RecoverForm
from application import CONFIG

@mod_user.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm(request.form)
	if request.method == "POST" and form.validate():
		try:
			controller.login(request.form["email"], request.form["password"])
			return redirect("/account")
		except Exception as e:
			exceptionType = e.args[0]
			if exceptionType == "AuthenticationError":
				flash("Invalid email and/or password.", "error")
			else:
				if(CONFIG["DEBUG"]):
					raise e
				else:
					flash("Something went wrong.", "error")
	return render_template("user_login.html", form = form)

@mod_user.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
	controller.logout()
	return redirect("/")

@mod_user.route("/forgot", methods=["GET", "POST"])
def recover():
	form = EmailForm(request.form)
	if request.method == "POST" and form.validate():
		try:
			controller.send_recovery_email(request.form["email"])
			flash("Email sent to " + request.form["email"] + '.', 'success')
		except Exception as e:
			exceptionType = e.args[0]
			if exceptionType == "UserDoesNotExistError":
				flash("No account exists with that email.", "error")
			else:
				if CONFIG["DEBUG"]:
					raise e
				else:
					flash("Something went wrong." , "error")
	return render_template("user_forgot.html", form = form)

@mod_user.route("/recover/<token>", methods=["GET", "POST"])
def recover_change(token):
	email = controller.detokenize_email(token)

	form = RecoverForm(request.form)
	if request.method == "POST" and form.validate():
		try:
			controller.change_password(email, request.form["password"])
			flash("Password changed.", "sucess")
			return redirect("/")
		except Exception as e:
			if CONFIG["DEBUG"]:
				raise e
			else:
				flash("Something went wrong.", "error")
	return render_template("user_recover.html", email = email, form = form)

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
			return redirect("/")
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

@mod_user.route("/confirm/<token>")
def confirm_email(token):
	controller.confirm_email(token)
	return redirect("/?status=confirmed")
