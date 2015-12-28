from flask import render_template, redirect, request, flash
from . import user_module as mod_user
from . import controllers as controller
from .forms import RegistrationForm
from application import CONFIG

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
				if CONFIG["Debug"]:
					raise e
				else:
					flash("Something went wrong.", "error")
	return render_template("user_register.html", form = form)

@mod_user.route("/confirm/<token>")
def confirm_email(token):
	controller.confirm_email(token)
	return redirect("/?status=confirmed");
