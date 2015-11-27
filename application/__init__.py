from flask import Flask
from mongoengine import register_connection

app = Flask(
    __name__,
    static_folder="static"
)

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

register_connection(
    alias = 'db', 
    name = CONFIG['DB_NAME'],
    username = CONFIG['DB_USERNAME'],
    password = CONFIG['DB_PASSWORD'],
    host = CONFIG['DB_HOST'],
    port = CONFIG['DB_PORT']
)

from application.mod_web import web_module
app.register_blueprint(web_module)
from application.mod_user import user_module
app.register_blueprint(user_module)