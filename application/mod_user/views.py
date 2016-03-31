from flask import render_template, redirect, request, flash, session
from flask.ext.login import login_required, current_user
from . import user_module as mod_user
from . import controllers as controller
from .forms import *
from application import CONFIG
from application import cache
import json

@cache.cached()
@mod_user.route("/login", methods=["GET", "POST"])
def login():
  if current_user.is_authenticated:
    return redirect("/account")

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
          if request.args.get("next") is not None:
            return redirect(request.args.get("next"))
          return redirect("/account")
    except Exception as e:
      if(CONFIG["DEBUG"]):
        raise e
      else:
        flash("Something went wrong.", "error")
  return render_template("user.login.html", form = form)

@mod_user.route("/logout", methods=["GET", "POST"])
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
      flash("Password changed.", "success")
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

  controller.logout();

  confirmed = controller.get_user_attr(email, "confirmed")

  return render_template("user.confirm.html")

@mod_user.route("/account/confirm/<token>")
def confirm_email(token):
  session.pop("email", None)
  controller.confirm_email(token)
  flash("Account confirmed! Login to start your application!", "success")
  return redirect("/account/application")

@mod_user.route("/account/settings", methods = ["GET", "POST"])
@login_required
def settings():
  name_form = ChangeNameForm(request.form)
  password_form = ChangePasswordForm(request.form)
  if request.method == "POST":
    if request.form["setting"] == "name" and name_form.validate():
      try:
        controller.change_name(current_user.email, request.form["firstname"], request.form["lastname"])
        flash("Name changed.", "success")
      except Exception as e:
        if CONFIG["DEBUG"]:
          raise e
        else:
          flash("Something went wrong.", "error")
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
      else:
        flash("Incorrect password.", "error")
    if request.form["setting"] == "type_account":
      if current_user.status == "Submitted":
        flash("Application already submitted.", "error")
      else:
        try:
          controller.change_account_type(current_user.email, request.form["type_account"])
          flash("Account type changed.", "success")
        except Exception as e:
          if CONFIG["DEBUG"]:
            raise e
          else:
            flash("Something went wrong.", "error")
    if request.form["setting"] == "delete_account":
      try:
        controller.delete_account(current_user.email)
        flash("Account deleted.", "success")
        return redirect("/")
      except Exception as e:
        if CONFIG["DEBUG"]:
          raise e
        else:
          flash("Something went wrong.", "error")
  else:
    user = controller.get_user(current_user.email)
    name_form = ChangeNameForm(request.form, obj = user)
  return render_template("user.settings.html", name_form = name_form, password_form = password_form)

@cache.cached()
@mod_user.route("/register", methods = ["GET", "POST"])
def register():
  if current_user.is_authenticated:
    return redirect("/account")

  if not CONFIG["HACKER_REGISTRATION_ENABLED"] and not CONFIG["MENTOR_REGISTRATION_ENABLED"]:
    flash("Registration is not open at this time.", "error")
    return redirect("/")

  form = RegistrationForm(request.form)
  if request.method == "POST" and form.validate():
    type_account = request.form["type_account"]

    if type_account == "hacker" and not CONFIG["HACKER_REGISTRATION_ENABLED"]:
      flash("Hacker registration is not open at this time.", "error")
      return render_template("user.register.html", form = form)
    if type_account == "mentor" and not CONFIG["MENTOR_REGISTRATION_ENABLED"]:
      flash("Mentor registration is not open at this time.", "error")
      return render_template("user.register.html", form = form)

    try:
      controller.add_user(request.form["email"], request.form["first_name"], request.form["last_name"], request.form["password"], request.form["type_account"])
      flash("Check your inbox for an email to confirm your account!", "success")
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

@cache.cached()
@mod_user.route("/scholarship", methods = ["GET", "POST"])
def scholarship():
  if current_user.is_authenticated:
    return redirect("/account")

  if not CONFIG["SCHOLARSHIP_REGISTRATION_ENABLED"]:
    flash("Scholarship registration is not open at this time.", "error")
    return redirect("/")

  form = ScholarshipRegistrationForm(request.form)
  if request.method == "POST" and form.validate():
    try:
      controller.add_user(request.form["email"], request.form["first_name"], request.form["last_name"], request.form["password"], "scholarship")
      flash("Check your inbox for an email to confirm your account!", "success")
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
  return render_template("user.scholarship.html", form = form)

@mod_user.route("/account/rsvp", methods = ["GET", "POST"])
@login_required
def rsvp():
    if current_user.decision != "Accepted":
      return redirect("/account")
    if current_user.type_account == "mentor":
      form = MentorRsvpForm(request.form)
    else:
      form = RsvpForm(request.form)
    rsvp_submitted = controller.get_user_attr(current_user.email, "rsvp")

    if request.method == "POST":
      try:
        if not rsvp_submitted:
          if "save" in request.form:
            controller.save_form_data(current_user.email, request.form)
            flash("Saved.", "success")
          elif "submit" in request.form:
            controller.save_form_data(current_user.email, request.form)
            if ('attending' in request.form and request.form['attending'] == 'Not Attending') or form.validate():
              flash("Submitted.", "success")
              controller.set_user_attr(current_user.email, "rsvp", True)
              controller.login(current_user.email) #To immediately update application status and disable the form
            else:
              flash("Please correct any errors.", "error")
          else:
            if CONFIG["DEBUG"]:
              flash("You didn't seem to tell us to do anything.", "error")
      except Exception as e:
        if CONFIG["DEBUG"]:
          raise e
        flash("Something went wrong.", "error")
    else:
      user = controller.get_user(current_user.email)
      if current_user.type_account == "mentor":
        form = MentorRsvpForm(request.form, obj = user)
      else:
        form = RsvpForm(request.form, obj = user)
    return render_template("user.rsvp.html", form = form, can_edit = not rsvp_submitted)

@mod_user.route("/account/application", methods = ["GET", "POST"])
@login_required
def application():
  if current_user.type_account == "mentor":
    form = MentorApplicationForm(request.form)
  elif current_user.type_account == "scholarship":
    form = ScholarshipApplicationForm(request.form)
  else:
    form = ApplicationForm(request.form)
  if request.method == "POST":
    try:
      applicationStatus = controller.get_user_attr(current_user.email, "status")

      if applicationStatus in ["Not Started", "In Progress"]:
        if "save" in request.form:
          controller.save_form_data(current_user.email, request.form)
          controller.set_user_attr(current_user.email, "status", "In Progress")
          flash("Application Saved", "success")
        elif "submit" in request.form:
          controller.save_form_data(current_user.email, request.form)
          if form.validate():
            flash("Application Submitted", "success")
            if not CONFIG["DEBUG"]:
              controller.set_user_attr(current_user.email, "status", "Submitted")
            if current_user.type_account == "mentor" and CONFIG["AUTO_ACCEPT_MENTORS"]:
              controller.accept_applicant(current_user.uid)
            controller.login(current_user.email) #To immediately update application status and disable the form
          else:
            flash("Please correct any errors in your application.", "error")
    except Exception as e:
      if CONFIG["DEBUG"]:
        raise e
      flash("Something went wrong.", "error")
  else:
    user = controller.get_user(current_user.email)
    if current_user.type_account == "mentor":
      form = MentorApplicationForm(request.form, obj = user)
    elif current_user.type_account == "scholarship":
      form = ScholarshipApplicationForm(request.form, obj = user)
    else:
      form = ApplicationForm(request.form, obj = user)
  return render_template("user.application.html", form = form)

@mod_user.route("/paths", methods = ["GET", "POST"])
@login_required
def path_base():
  user = controller.get_user(current_user.email)
  registration_open = controller.get_app_setting("path_registration_open")

  if request.method == "POST":
    if "register" in request.form:
      path_name = request.form["register"]
      if current_user.type_account == "mentor":
        flash("Mentors cannot register for paths.", "error")
      else:
        if registration_open:
          if user.path == path_name:
            flash("You are already registered for this path!", "error")
          elif user.path in ["code-for-good", "ios", "web-dev"]: 
            flash("You are already registered for another path!", "error")
          else:
            space_left = controller.path_spots_left(path_name)
            if space_left == 0:
              flash("Sorry, this path has been filled!", "error")
            else:
              controller.register_user_for_path(current_user.email, path_name)
              flash("You have sucessfully registered!", "success")
        else:
          flash("Path registration is currently closed.", "error")
    elif "leave-path" in request.form:
      print("here")
      if user.path not in ["code-for-good", "ios", "web-dev"]: 
        flash("You are not currently registered for a path!", "error")
      else:
        controller.user_leave_path(current_user.email)
        flash("Path left.", "success")
  user = controller.get_user(current_user.email)
  return render_template("user.paths_base.html", user_path = user.path, registration_open = registration_open)

@mod_user.route("/paths/<path_name>", methods = ["GET", "POST"])
@login_required
def path_specific(path_name):
  user = controller.get_user(current_user.email)
  registration_open = controller.get_app_setting("path_registration_open")

  if request.method == "POST":
    if "register" in request.form:
      if current_user.type_account == "mentor":
        flash("Mentors cannot register for paths.", "error")
      else:
        if registration_open:
          if user.path == path_name:
            flash("You are already registered for this path!", "error")
          elif user.path in ["code-for-good", "ios", "web-dev"]: 
            flash("You are already registered for another path!", "error")
          else:
            space_left = controller.path_spots_left(path_name)
            if space_left == 0:
              flash("Sorry, this path has been filled!", "error")
            else:
              controller.register_user_for_path(current_user.email, path_name)
              flash("You have sucessfully registered!", "success")
        else:
          flash("Path registration is currently closed.", "error")
    elif "leave-path" in request.form:
      if user.path not in ["code-for-good", "ios", "web-dev"]: 
        flash("You are not currently registered for a path!", "error")
      else:
        controller.user_leave_path(current_user.email)
        flash("Path left.", "success")

  user = controller.get_user(current_user.email)
  return render_template("user.paths_specific.html", path_name = path_name, user_path = user.path, registration_open = registration_open)
