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

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

from application import views
from application import models

from application.belts import views, models

from application.senseis import views, models

from application.topics import views, models

from application.events import views, models

from application.auth import models, views
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try: 
    db.create_all()
except:
    pass

pw_hashed = "$2b$12$JeYUxbSj8d0kqu406NZv3OhUu7Ln32nPj2twGnS8LXzhcAsDkF7ty"

user = User.query.filter_by(username="genki").first()
if not user:
    admin = User("Genki Sudo", "genki", pw_hashed)
    db.session.add(admin)
    db.session.commit()
elif user.password != pw_hashed:
    user.password = pw_hashed
    db.session.commit()