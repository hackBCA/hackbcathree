from flask import render_template
from flask.ext.login import login_required, current_user
from . import live_module as mod_live
from application import CONFIG

@mod_live.route("/live", methods = ["GET", "POST"])
def live():
    return render_template("live.live.html", broadcast_url = CONFIG["BROADCAST_URL"])