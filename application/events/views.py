from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.models import Events
from application.forms import EventForm
import datetime

from sqlalchemy.sql.expression import select

@app.route("/events", methods=["GET"])
def events_index():
    e = Events.query.order_by(Events.day, Events.time).all()
    b = Events.belts_for_event()
    t = Events.topics_for_event()
    return render_template("events/list.html", events = e, belts = b, topics = t)

@app.route("/events/new/")
@login_required
def events_form():
    return render_template("events/new.html", form = EventForm())

@app.route("/events/", methods=["POST"])
@login_required
def events_create():
    form = EventForm(request.form)
    d = form.day.data
    if d == None:
        d = datetime.datetime.now().strftime("%Y-%m-%d") # formerly "%d.%m.%Y"
    else:
        d = d.strftime("%Y.%m.%d") # "%d.%m.%Y"
    e = Events(form.name.data, d, form.time.data, form.info.data)

    db.session().add(e)
    db.session().commit()
  
    return redirect(url_for("events_index"))

@app.route("/events/<id>", methods=["POST"])
@login_required
def edit_events(id):
    e = Events.query.get(id)
    belts = Events.belts_for_event_id(id)
    nb = Events.belts_for_event_not_id(id)
    t = Events.topics_for_event_id(id)
    nt = Events.topics_for_event_not_id(id)
    return render_template("events/edit.html", events = e, form = EventForm(), belts = belts, not_belts = nb, topics = t, not_topics = nt)

@app.route("/events/<id>/addbelt/<b_id>", methods=["POST"])
@login_required
def add_belt(id, b_id):
    Events.add_belt(id, b_id)
    e = Events.query.get(id)
    belts = Events.belts_for_event_id(id)
    nb = Events.belts_for_event_not_id(id)
    t = Events.topics_for_event_id(id)
    nt = Events.topics_for_event_not_id(id)
    return render_template("events/edit.html", events = e, form = EventForm(), belts = belts, not_belts = nb, topics = t, not_topics = nt)

@app.route("/events/<id>/delbelt/<b_id>", methods=["POST"])
@login_required
def del_belt(id, b_id):
    Events.delete_belt(id, b_id)
    e = Events.query.get(id)
    belts = Events.belts_for_event_id(id)
    nb = Events.belts_for_event_not_id(id)
    t = Events.topics_for_event_id(id)
    nt = Events.topics_for_event_not_id(id)
    return render_template("events/edit.html", events = e, form = EventForm(), belts = belts, not_belts = nb, topics = t, not_topics = nt)

@app.route("/events/<id>/addtopic/<t_id>", methods=["POST"])
@login_required
def add_topic(id, t_id):
    Events.add_topic(id, t_id)
    e = Events.query.get(id)
    belts = Events.belts_for_event_id(id)
    nb = Events.belts_for_event_not_id(id)
    t = Events.topics_for_event_id(id)
    nt = Events.topics_for_event_not_id(id)
    return render_template("events/edit.html", events = e, form = EventForm(), belts = belts, not_belts = nb, topics = t, not_topics = nt)

@app.route("/events/<id>/deltopic/<t_id>", methods=["POST"])
@login_required
def del_topic(id, t_id):
    Events.delete_topic(id, t_id)
    e = Events.query.get(id)
    belts = Events.belts_for_event_id(id)
    nb = Events.belts_for_event_not_id(id)
    t = Events.topics_for_event_id(id)
    nt = Events.topics_for_event_not_id(id)
    return render_template("events/edit.html", events = e, form = EventForm(), belts = belts, not_belts = nb, topics = t, not_topics = nt)

@app.route("/events/ed/<id>", methods=["POST"])
@login_required
def mod_events(id):
    form = EventForm(request.form)
    name = form.name.data
    d = form.day.data
    t = form.time.data
    i = form.info.data
    e = Events.query.get(id)
    if d != "" and d == None:
        e.day = datetime.datetime.now().strftime("%Y-%m-%d") #formerly "%d.%m.%Y"
    elif d != "":
        d = d.strftime("%Y-%m-%d")
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
@login_required
def events_del(id):
    t = Events.query.get(id)
    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("events_index"))