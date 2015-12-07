from application import CONFIG, app
from .models import *
from flask import LoginManager

staff_login_manager = LoginManager()

staff_login_manager.init(app)

@staff_login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)
