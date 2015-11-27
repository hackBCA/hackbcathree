from flask import *
from . import web_module as mod_web
from . import controllers as controller

@mod_web.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		if request.form["email"]:
			email = request.form["email"]
			try:
				controller.add_email(email)
			except Exception as e:
				if(e.args[0] == 'EmailExistsError'):
					return render_template("index.html", error = e.args[1])
				pass
			return render_template("index.html", message = 'Verification email sent.')
	if request.args.get('status'):
		status = request.args.get('status')
		if status == 'confirmed':
			return render_template("index.html", message = "Subscription confirmed.")
	return render_template("index.html")

@mod_web.route("/sponsors",methods=["GET"])
def sponsors():
    return mod_web.send_static_file("sponsors.pdf")

@mod_web.route("/sponsors.pdf",methods=["GET"])
def foward_sponsors():
    return redirect("/sponsors")

@mod_web.route('/confirm/<token>')
def confirm_email(token):
	controller.confirm_email(token);
	return redirect('/?status=confirmed');