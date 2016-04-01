from flask import Blueprint

live_module = Blueprint(
    "live",
    __name__,
    url_prefix = "",
    template_folder = "templates",
    static_folder = "live_static"
)

from . import views
