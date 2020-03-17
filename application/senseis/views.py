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