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

@app.route("/belts/<id>", methods=["POST"])
def edit_belts(id):
    return render_template("belts/edit.html", belts = Belts.query.get(id))

@app.route("/belts/", methods=["POST"])
def mod_belts(id):
    belt = request.form.get("belt")
    if len(belt) == 0:
        return redirect(url_for("belts_index"))
    else:
        b = Belts.query.get(id)
        b.belt = belt
        db.session().commit()
        return redirect(url_for("belts_index"))

@app.route("/belts/del/<id>", methods=["POST"])
def belts_del(id):
    b = Belts.query.get(id)

    db.session().delete(b)
    db.session().commit()
  
    return redirect(url_for("belts_index"))