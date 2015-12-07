from flask import Blueprint

staff_module = Blueprint(
    "staff", 
    __name__, 
    url_prefix = "/staff",
    template_folder = "staff_templates",
    static_folder = "staff_static"
)

from . import views