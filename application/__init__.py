from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, MetaData # POIS POIS
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

db.create_all()

user = User.query.filter_by(username="genki", password="sudo3").first()
if not user:
    admin = User("Genki Sudo", "genki", "sudo3")
    db.session.add(admin)
    db.session.commit()