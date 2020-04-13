from application import app, db, login_required, login_manager
from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.models import Senseis
from application.forms import SenseiForm
from application.auth.models import User
from application.auth.hasher import hasher, checker
from sqlalchemy.sql import func

@app.route("/senseis", methods=["GET"])
def senseis_index():
    return render_template("senseis/list.html", senseis = Senseis.query.order_by(func.lower(Senseis.name)).all())

@app.route("/senseis/new/")
@login_required
def senseis_form():
    return render_template("senseis/new.html", form = SenseiForm())

@app.route("/senseis/", methods=["POST"])
@login_required
def senseis_create():
    form = SenseiForm(request.form)
    logon = form.logon.data.lower().rstrip()
    prior_sensei = Senseis.query.filter_by(logon=logon).first()

    if logon == 'genki':
        return render_template("senseis/new.html", form = form, error = "Sorry, 'Genki' reserverd for other purposes")
    elif not form.validate():
        return render_template("senseis/new.html", form = SenseiForm(), error = "Name and Logon should be between 3 and 15 char")
    elif len(form.logon.data.strip()) < 3:
        return render_template("senseis/new.html", form = SenseiForm(), error = "Blanks in logon don't count, you need at least 3 char")
    elif prior_sensei:
        return render_template("senseis/new.html", form = SenseiForm(), error = "Logon already taken")
    
    s = Senseis(form.name.data, form.logon.data.lower())
    u = User(form.name.data, logon, hasher("newuser"))
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
    s = Senseis.query.get(id)
    if not (current_user.id == s.id or current_user.username == 'genki'):
        return login_manager.unauthorized()

    form = SenseiForm(request.form)
    name = form.name.data
    l = form.logon.data.lower().strip()
    prior_sensei = Senseis.query.filter_by(logon=l).first()
    same = (s == prior_sensei)

    if l == 'genki':
        return render_template("senseis/edit.html", senseis = Senseis.query.get(id), error = "Sorry, 'Genki' reserverd for other purposes")
    elif not form.validate() and len(name.strip()) > 0 and len(l) > 0:
        return render_template("senseis/edit.html", senseis = Senseis.query.get(id), error = "Name and Logon should be between 3 and 15 char")
    elif len(name.strip()) > 0 and len(name.strip()) < 3:
        return render_template("senseis/edit.html", senseis = Senseis.query.get(id), error = "Name should be between 3 and 15 char without blanks")
    elif len(l) < 3 and len(l) > 0:
        return render_template("senseis/edit.html", senseis = Senseis.query.get(id), error = "Logon should be between 3 and 15 char without blanks")
    elif prior_sensei and not same:
        return render_template("senseis/edit.html", senseis = Senseis.query.get(id), error = "Logon already taken")

    
    user = User.query.filter_by(username=s.logon).first()
    if len(name.strip()) > 0:
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