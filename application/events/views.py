from application import app, db
from flask import redirect, render_template, request, url_for
from application.models import Events

@app.route("/events", methods=["GET"])
def events_index():
    return render_template("events/list.html", events = Events.query.all())

@app.route("/events/new/")
def events_form():
    return render_template("events/new.html")

@app.route("/events/", methods=["POST"])
def events_create():
    t = Events(request.form.get("name"), request.form.get("day"), request.form.get("time"), request.form.get("info"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("events_index"))

@app.route("/events/<id>", methods=["POST"])
def edit_events(id):
    return render_template("events/edit.html", events = Events.query.get(id))

@app.route("/events/ed/<id>", methods=["POST"])
def mod_events(id):
    name = request.form.get("name")
    d = request.form.get("day")
    t = request.form.get("time")
    i = request.form.get("info")
    e = Events.query.get(id)
    if len(name) > 0:
        e.name = name
    if len(d) > 0:
        e.day = d
    if len(t) > 0:
        e.time = t
    if len(i) > 0:
        e.info = i
    db.session().commit()
    return redirect(url_for("events_index"))

@app.route("/events/del/<id>", methods=["POST"])
def events_del(id):
    t = Events.query.get(id)

    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("events_index"))