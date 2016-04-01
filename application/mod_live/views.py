from flask import render_template, request
from flask.ext.login import login_required, current_user
from . import live_module as mod_live
from application import CONFIG
from application.mod_web import controllers as web_controllers

@mod_live.route("/live", methods = ["GET", "POST"])
def live():
    schedule = web_controllers.get_schedule()
    return render_template(
                "live.live.html", 
                broadcast_url = CONFIG["BROADCAST_URL"], 
                session = request.cookies.get("session"),
                schedule = schedule
            )