from flask import render_template, redirect, request, flash, session
from flask.ext.login import login_required, current_user
from . import user_module as mod_user
from . import controllers as controller
from .forms import *
from application import CONFIG
from application import cache

@cache.cached()
@mod_user.route("/login", methods=["GET", "POST"])
def login():
  form = LoginForm(request.form)
  if request.method == "POST" and form.validate():
    try:  
      if controller.verify_user(request.form["email"], request.form["password"]) is None:
        flash("Invalid email and/or password.", "error")
      else:    
        confirmed = controller.get_user_attr(request.form["email"], "confirmed")

        if not confirmed:
          session["email"] = request.form["email"]
          return redirect("/account/confirm")
        else:
          controller.login(request.form["email"])
          return redirect("/account")
    except Exception as e:
      if(CONFIG["DEBUG"]):
        raise e
      else:
        flash("Something went wrong.", "error")
  return render_template("user.login.html", form = form)

@mod_user.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
  controller.logout()
  return redirect("/")

@cache.cached()
@mod_user.route("/forgot", methods = ["GET", "POST"])
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
  return render_template("user.forgot.html", form = form)

@mod_user.route("/recover/<token>", methods = ["GET", "POST"])
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
  return render_template("user.recover.html", email = email, form = form)

@mod_user.route("/account")
@login_required
def account():
  return render_template("user.account.html")

@mod_user.route("/account/confirm", methods = ["GET", "POST"])
def verify():
  if "email" not in session:
    return redirect("/")

  email = session["email"]

  if request.method == "POST":
    controller.validate_email(email)
    flash("Almost there! Confirmation email resent.", "neutral")
    return redirect("/login")

  confirmed = controller.get_user_attr(email, "confirmed")
  
  return render_template("user.confirm.html")

@mod_user.route("/account/confirm/<token>")
def confirm_email(token):
  session.pop("email", None)
  controller.confirm_email(token)
  flash("Account confirmed!", "success")
  return redirect("/?status=confirmed")

@mod_user.route("/account/settings", methods = ["GET", "POST"])
@login_required
def settings():
  password_form = ChangePasswordForm(request.form)
  if request.method == "POST":
    if request.form["setting"] == "password" and password_form.validate():
      if controller.verify_user(current_user.email, request.form["password"]) is not None:
        try:
          controller.change_password(current_user.email, request.form["new_password"])
          flash("Password changed.", "success")
        except Exception as e:
          if CONFIG["DEBUG"]:
            raise e
          else:
            flash("Something went wrong.", "error")
  return render_template("user.settings.html", password_form = password_form)

@cache.cached()
@mod_user.route("/register", methods = ["GET", "POST"])
def register():
  form = RegistrationForm(request.form)
  if request.method == "POST" and form.validate():
    try:
      controller.add_user(request.form["email"], request.form["first_name"], request.form["last_name"], request.form["password"])
      flash("Almost there! Check your inbox for an email to confirm your account.", "success")
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
  return render_template("user.register.html", form = form)

@mod_user.route("/account/application", methods = ["GET", "POST"])
@login_required
def application():
  form = ApplicationForm(request.form)
  if request.method == "POST":
    try:
      applicationStatus = controller.get_user_attr(current_user.email, "status")

      if applicationStatus in ["Not Started", "In Progress"]:
        if "save" in request.form:
          controller.save_application(current_user.email, request.form) 
        elif "submit" in request.form:
          controller.save_application(current_user.email, request.form) 
          if form.validate():
            a = 1
            #controller.set_user_attr(current_user.email, "status", "Submitted")
    except Exception as e:
      if CONFIG["DEBUG"]:
        raise e
      flash("Something went wrong.", "error")
  else:
    user = controller.get_user(current_user.email)
    form = ApplicationForm(obj = user)  
  return render_template("user.application.html", form = form)

