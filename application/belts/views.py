from application import app, db
from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required
from application.events.models import Events
from application.belts.models import Belts
from application.forms import BeltForm
import datetime

@app.route("/belts", methods=["GET"])
def belts_index():
    ne = Events.belts_without_event()
    return render_template("belts/list.html", belts = Belts.query.order_by(Belts.belt).all(), no_events = ne)

@app.route("/belts/new/")
@login_required
def belts_form():
    return render_template("belts/new.html", form = BeltForm())

@app.route("/belts/", methods=["POST"])
@login_required
def belts_create():
    form = BeltForm(request.form)
    prior_belt = Belts.query.filter_by(belt=form.belt.data).first()

    if not form.validate():
        return render_template("belts/new.html", form = form)
    elif len(form.belt.data.strip()) < 3:
        form.belt.errors.append("Blanks don't count, have at least 3 char")
        return render_template("belts/new.html", form = form)
    elif prior_belt:
        form.belt.errors.append("Such belt already exists")
        return render_template("belts/new.html", form = form)

    b = Belts(form.belt.data)
    db.session().add(b)
    db.session().commit()
    flash("Belt '{}' was created".format(b.belt))
    return redirect(url_for("belts_index"))

@app.route("/belts/<id>", methods=["POST"])
@login_required
def edit_belts(id):
    return render_template("belts/edit.html", belts = Belts.query.get(id))

@app.route("/belts/<id>/events", methods=["GET"])
def list_belt_events(id):
    belt = Belts.query.get(id)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    week = (datetime.datetime.now() + datetime.timedelta(days=14)).strftime("%Y-%m-%d")
    e = Events.query.order_by(Events.day, Events.time).filter(Events.belts.contains(belt), Events.day >= today, Events.day < week).all()
    for ev in e:
        date_obj = datetime.datetime.strptime(ev.day, "%Y-%m-%d")
        ev.day = date_obj.strftime("%a %d.%m.%Y")
    q = "for the next 14 days"
    return render_template("belts/events_for_belt.html", events = e, Belt = belt, qualification = q)

@app.route("/belts/<id>/allevents", methods=["GET"])
def list_all_belt_events(id):
    belt = Belts.query.get(id)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    e = Events.query.order_by(Events.day, Events.time).filter(Events.belts.contains(belt), Events.day >= today).all()
    for ev in e:
        date_obj = datetime.datetime.strptime(ev.day, "%Y-%m-%d")
        ev.day = date_obj.strftime("%a %d.%m.%Y")
    q = "in the future"
    return render_template("belts/events_for_belt.html", events = e, Belt = belt, qualification = q)

@app.route("/belts/del/<id>", methods=["POST"])
@login_required
def belts_del(id):
    b = Belts.query.get(id)
    flash("Belt '{}' was deleted".format(b.belt))
    db.session().delete(b)
    db.session().commit()
  
    return redirect(url_for("belts_index"))