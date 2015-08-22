from flask import Flask

app = Flask(__name__, static_folder="static", static_url_path="")
app.config.from_pyfile("../config.cfg")

CONFIG = app.config

DEBUG = CONFIG["DEBUG"]

from . import views