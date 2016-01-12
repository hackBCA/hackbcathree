from flask import Blueprint

web_module = Blueprint(
    "web", 
    __name__, 
    url_prefix = "",
    template_folder = "templates",
    static_folder = "web_static"
)

from . import views