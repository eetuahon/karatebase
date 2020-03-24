from application import app, db
from flask import redirect, render_template, request, url_for
from application.models import Events
from application.forms import EventForm
import datetime

@app.route("/events", methods=["GET"])
def events_index():
    return render_template("events/list.html", events = Events.query.all())

@app.route("/events/new/")
def events_form():
    return render_template("events/new.html", form = EventForm())

@app.route("/events/", methods=["POST"])
def events_create():
    form = EventForm(request.form)
    d = form.day.data
    if d == None:
        d = datetime.datetime.now().strftime("%d.%m.%Y")
    else:
        d = d.strftime("%d.%m.%Y")
    e = Events(form.name.data, d, form.time.data, form.info.data)

    db.session().add(e)
    db.session().commit()
  
    return redirect(url_for("events_index"))

@app.route("/events/<id>", methods=["POST"])
def edit_events(id):
    return render_template("events/edit.html", events = Events.query.get(id), form = EventForm())

@app.route("/events/ed/<id>", methods=["POST"])
def mod_events(id):
    form = EventForm(request.form)
    name = form.name.data
    d = form.day.data
    t = form.time.data
    i = form.info.data
    e = Events.query.get(id)
    if d != "" and d == None:
        e.day = datetime.datetime.now().strftime("%d.%m.%Y")
    elif d != "":
        d = d.strftime("%d.%m.%Y")
        e.day = d
    if len(name) > 0:
        e.name = name
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