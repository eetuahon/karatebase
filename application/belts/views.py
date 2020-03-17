from application import app, db
from flask import redirect, render_template, request, url_for
from application.models import Belts

@app.route("/belts", methods=["GET"])
def belts_index():
    return render_template("belts/list.html", belts = Belts.query.all())

@app.route("/belts/new/")
def belts_form():
    return render_template("belts/new.html")

@app.route("/belts/", methods=["POST"])
def belts_create():
    t = Belts(request.form.get("belt"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("belts_index"))