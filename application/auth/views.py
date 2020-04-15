from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, ChangeForm
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
                               error = "No such username or incorrect password")

    if checker(user.password, pw) == False:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or incorrect password")

    login_user(user)
    flash("Otagai ni rei, sensei ni rei, welcome to the dojo {}".format(user.name))
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/changepw", methods = ["GET", "POST"])
@login_required(role="SENSEI")
def change_pw():
    if request.method == "GET":
        return render_template("auth/changepw.html", form = ChangeForm())

    form = ChangeForm(request.form)
    old = form.old.data
    new1 = form.new1.data
    new2 = form.new2.data

    user = User.query.filter_by(username=current_user.username).first()
    if checker(user.password, old) == False:
        return render_template("auth/changepw.html", form = form,
                               error = "Current password wrong!")
    
    if (new1 != new2):
        return render_template("auth/changepw.html", form = form,
                               error = "New passwords must match to avoid typos")
    elif not form.validate():
        return render_template("auth/changepw.html", form = form,
                               error = "New password should be 8 to 64 char long")
    
    new_pw = hasher(new1)
    user.password = new_pw
    db.session().commit()
    login_user(user)
    flash("Password changed successfully, the old password is no longer valid")
    return redirect(url_for("index"))