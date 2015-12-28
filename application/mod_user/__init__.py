from flask import Blueprint

user_module = Blueprint(
    "user",
    __name__,
    url_prefix = "",
    template_folder = "user_templates",
    static_folder = "user_static"
)

from . import views
