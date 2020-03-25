from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.models import Senseis
from application.forms import SenseiForm

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
    s = Senseis(form.name.data, form.logon.data)
    db.session().add(s)
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
    l = form.logon.data
    s = Senseis.query.get(id)
    if len(name) > 0 or len(l) == 0:
        s.name = name
    if len(l) > 0:
        s.logon = l
    db.session().commit()
    return redirect(url_for("senseis_index"))

@app.route("/senseis/del/<id>", methods=["POST"])
@login_required
def senseis_del(id):
    t = Senseis.query.get(id)

    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("senseis_index"))