from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.models import Senseis
from application.forms import SenseiForm
from application.auth.models import User
from application.auth.hasher import hasher, checker

@app.route("/senseis", methods=["GET"])
def senseis_index():
    return render_template("senseis/list.html", senseis = Senseis.query.order_by(Senseis.name).all())

@app.route("/senseis/new/")
@login_required
def senseis_form():
    return render_template("senseis/new.html", form = SenseiForm())

@app.route("/senseis/", methods=["POST"])
@login_required
def senseis_create():
    form = SenseiForm(request.form)
    s = Senseis(form.name.data, form.logon.data.lower())
    u = User(form.name.data, form.logon.data.lower(), hasher("newuser"))
    db.session().add(s)
    db.session().add(u)
    db.session().commit()
  
    return redirect(url_for("senseis_index"))


@app.route("/senseis/<id>", methods=["POST"])
@login_required
def edit_senseis(id):
    return render_template("senseis/edit.html", senseis = Senseis.query.get(id))

@app.route("/senseis/ed/<id>", methods=["POST"])
@login_required
def mod_senseis(id):
    form = SenseiForm(request.form)
    name = form.name.data
    l = form.logon.data.lower()
    s = Senseis.query.get(id)
    user = User.query.filter_by(username=s.logon).first()
    if len(name) > 0 or len(l) == 0:
        s.name = name
        user.name = name
    if len(l) > 0:
        s.logon = l
        user.username = l
    db.session().commit()
    return redirect(url_for("senseis_index"))

@app.route("/senseis/del/<id>", methods=["POST"])
@login_required
def senseis_del(id):
    t = Senseis.query.get(id)
    logon = t.logon
    user = User.query.filter_by(username=logon).first()

    db.session().delete(t)
    db.session().delete(user)
    db.session().commit()
  
    return redirect(url_for("senseis_index"))