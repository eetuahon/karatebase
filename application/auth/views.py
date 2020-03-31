from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.hasher import hasher, checker

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    pw = form.password.data
    

    user = User.query.filter_by(username=form.username.data.lower()).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    if checker(user.password, pw) == False:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))