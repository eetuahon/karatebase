from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)
f_bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///karatebase.db"    
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application import models
from application.belts import views
from application.senseis import views
from application.topics import views
from application.events import views

from application.auth import models, views

from application.auth.models import User
from application.auth.hasher import hasher, checker
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try: 
    db.create_all()
except:
    pass

pw_hashed = hasher("sudo3")

user = User.query.filter_by(username="genki").first()
if not user:
    admin = User("Genki Sudo", "genki", pw_hashed)
    db.session.add(admin)
    db.session.commit()
elif checker(user.password, "sudo3") == False:
    user.password = pw_hashed
    db.session.commit()