from application import app, db
from flask import redirect, render_template, request, url_for
from application.models import Senseis

@app.route("/senseis", methods=["GET"])
def senseis_index():
    return render_template("senseis/list.html", senseis = Senseis.query.all())

@app.route("/senseis/new/")
def senseis_form():
    return render_template("senseis/new.html")

@app.route("/senseis/", methods=["POST"])
def senseis_create():
    t = Senseis(request.form.get("name"), request.form.get("logon"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("senseis_index"))


@app.route("/senseis/<id>", methods=["POST"])
def edit_senseis(id):
    return render_template("senseis/edit.html", senseis = Senseis.query.get(id))

@app.route("/senseis/ed/<id>", methods=["POST"])
def mod_senseis(id):
    name = request.form.get("name")
    l = request.form.get("logon")
    s = Senseis.query.get(id)
    if len(name) > 0 or len(l) == 0:
        s.name = name
    if len(l) > 0:
        s.logon = l
    db.session().commit()
    return redirect(url_for("senseis_index"))

@app.route("/senseis/del/<id>", methods=["POST"])
def senseis_del(id):
    t = Senseis.query.get(id)

    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("senseis_index"))