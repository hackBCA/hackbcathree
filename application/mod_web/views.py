from flask import *
from . import web_module as mod_web
from . import controllers as controller

@mod_web.route("/", methods = ["GET", "POST"])
def index():
	if request.method == "POST":
		if request.form["email"]:
			email = request.form["email"]
			try:
				controller.add_email(email)
			except Exception as e:
				if(e.args[0] == "EmailExistsError"):
					flash(e.args[1], "error")
					return render_template("web.index.html")
				pass
			flash("Verification email sent.", "success")
			return render_template("web.index.html")
	if request.args.get("status"):
		status = request.args.get("status")
		if status == "confirmed":
			flash("Subscription confirmed.", "success")
			return render_template("web.index.html")
	return render_template("web.index.html")

@mod_web.route("/sponsors", methods = ["GET"])
def sponsors():
    return mod_web.send_static_file("sponsors.pdf")

@mod_web.route("/sponsors.pdf", methods = ["GET"])
def foward_sponsors():
    return redirect("/sponsors")

#mod_web.route("/confirm/<token>")
# def confirm_email(token):
# 	controller.confirm_email(token)
# 	return redirect("/?status=confirmed")