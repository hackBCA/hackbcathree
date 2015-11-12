from flask import Flask

app = Flask(__name__)

try:
    app.config.from_pyfile("../prod_config.cfg")
    print("Production configuration file loaded.")
except FileNotFoundError:
    print("Production configuration not found.")
    try:
        app.config.from_pyfile("../dev_config.cfg")
        print("Development configuration file loaded.")
        print("IF THIS IS PRODUCTION TERMINATE IMMEDIATELY!")
    except FileNotFoundError:
        print("Development configuration not found.")
        try:
            app.config.from_pyfile("../default_config.cfg")
            print("Default configuration file loaded.")
            print("IF THIS IS PRODUCTION TERMINATE IMMEDIATELY!")
        except FileNotFoundError:
            print("Default configuration not found.")
            print("No configuration files found.")

CONFIG = app.config

from application.mod_web import web_module
app.register_blueprint(web_module)