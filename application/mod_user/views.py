from flask import render_template, redirect
from . import user_module as mod_user

@mod_user.route("/user")
def index():
    return render_template("register.html")
