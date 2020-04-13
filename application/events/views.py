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
    for ev in e:
        date_obj = datetime.datetime.strptime(ev.day, "%Y-%m-%d")
        ev.day = date_obj.strftime("%a %d.%m.%Y")
    no_t = Events.events_without_topic()
    return render_template("events/list.html", events = e, no_topic = no_t)

@app.route("/events/new/")
@login_required
def events_form():
    return render_template("events/new.html", form = EventForm())

@app.route("/events/", methods=["POST"])
@login_required
def events_create():
    form = EventForm(request.form)
    prior_event = Events.query.filter_by(name=form.name.data).first()

    if not form.validate():
        return render_template("events/new.html", form = form)
    elif prior_event:
        form.name.errors.append("Such name already exists")
        return render_template("events/new.html", form = form)

    d = form.day.data
    if d == None:
        d = datetime.datetime.now().strftime("%Y-%m-%d")
    else:
        d = d.strftime("%Y-%m-%d")
    e = Events(form.name.data, d, form.time.data, form.info.data)

    db.session().add(e)
    db.session().commit()
  
    return redirect(url_for("events_index"))

@app.route("/events/<id>", methods=["POST", "GET"])
@login_required
def edit_events(id):
    e = Events.query.get(id)
    e_date = datetime.datetime.strptime(e.day, "%Y-%m-%d")
    e.day = e_date.strftime("%a %d.%m.%Y")
    return render_template("events/edit.html", events = e, form = EventForm())

@app.route("/events/<id>/addbelt/<b_id>", methods=["POST"])
@login_required
def add_belt(id, b_id):
    Events.add_belt(id, b_id)
    e = Events.query.get(id)
    e_date = datetime.datetime.strptime(e.day, "%Y-%m-%d")
    e.day = e_date.strftime("%a %d.%m.%Y")
    return render_template("events/edit.html", events = e, form = EventForm())

@app.route("/events/<id>/delbelt/<b_id>", methods=["POST"])
@login_required
def del_belt(id, b_id):
    Events.delete_belt(id, b_id)
    e = Events.query.get(id)
    e_date = datetime.datetime.strptime(e.day, "%Y-%m-%d")
    e.day = e_date.strftime("%a %d.%m.%Y")
    return render_template("events/edit.html", events = e, form = EventForm())

@app.route("/events/<id>/addtopic/<t_id>", methods=["POST"])
@login_required
def add_topic(id, t_id):
    Events.add_topic(id, t_id)
    e = Events.query.get(id)
    e_date = datetime.datetime.strptime(e.day, "%Y-%m-%d")
    e.day = e_date.strftime("%a %d.%m.%Y")
    return render_template("events/edit.html", events = e, form = EventForm())

@app.route("/events/<id>/deltopic/<t_id>", methods=["POST"])
@login_required
def del_topic(id, t_id):
    Events.delete_topic(id, t_id)
    e = Events.query.get(id)
    e_date = datetime.datetime.strptime(e.day, "%Y-%m-%d")
    e.day = e_date.strftime("%a %d.%m.%Y")
    return render_template("events/edit.html", events = e, form = EventForm())

@app.route("/events/<id>/addsensei/<s_id>", methods=["POST"])
@login_required
def add_sensei(id, s_id):
    Events.add_sensei(id, s_id)
    e = Events.query.get(id)
    e_date = datetime.datetime.strptime(e.day, "%Y-%m-%d")
    e.day = e_date.strftime("%a %d.%m.%Y")
    return render_template("events/edit.html", events = e, form = EventForm())

@app.route("/events/<id>/delsensei/<s_id>", methods=["POST"])
@login_required
def del_sensei(id, s_id):
    Events.delete_sensei(id, s_id)
    e = Events.query.get(id)
    e_date = datetime.datetime.strptime(e.day, "%Y-%m-%d")
    e.day = e_date.strftime("%a %d.%m.%Y")
    return render_template("events/edit.html", events = e, form = EventForm())

@app.route("/events/ed/<id>", methods=["POST"])
@login_required
def mod_events(id):
    form = EventForm(request.form)
    name = form.name.data
    d = form.day.data
    t = form.time.data
    i = form.info.data
    e = Events.query.get(id)
    prior_event = Events.query.filter_by(name=form.name.data).first()
    same = (e == prior_event)

    if (len(name) > 15 or (len(name) > 0 and len(name.strip()) < 3)) and (len(t) > 15 or (len(t) > 0 and len(t.strip()) < 3)):
        error = "Name and time should be between 3 and 15 char"
        return render_template("events/edit.html", events = e, form = EventForm(), error = error)
    elif (len(name) > 15 or (len(name) > 0 and len(name.strip()) < 3)):
        error = "Name should be between 3 and 15 char"
        return render_template("events/edit.html", events = e, form = EventForm(), error = error)
    elif prior_event and not same:
        error = "Event name already exists"
        return render_template("events/edit.html", events = e, form = EventForm(), error = error)
    elif (len(t) > 15 or (len(t) > 0 and len(t.strip()) < 3)):
        error = "Time should be between 3 and 15 char"
        return render_template("events/edit.html", events = e, form = EventForm(), error = error)

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