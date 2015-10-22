from flask import Flask

app = Flask(__name__)

# app.config.from_pyfile("../config.py")

from application.mod_web import web_module

app.register_blueprint(web_module)