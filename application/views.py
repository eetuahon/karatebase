from flask import render_template
from application import app
from flask_login import login_required, current_user
from application.events.models import Events
import datetime

@app.route("/")
def index():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    week = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    e = Events.query.order_by(Events.day, Events.time).filter(Events.day >= today, Events.day < week).all()
    for ev in e:
        date_obj = datetime.datetime.strptime(ev.day, "%Y-%m-%d")
        ev.day = date_obj.strftime("%a %d.%m.%Y")
    if current_user.is_authenticated:
        no_t = Events.events_without_topic()
        ne = Events.belts_without_event()
        for ev in no_t:
            date_obj = datetime.datetime.strptime(ev["day"], "%Y-%m-%d")
            ev["day"] = date_obj.strftime("%a %d.%m.%Y")
    else:
        no_t = ""
        ne = ""
    return render_template("index.html", events = e, no_topic = no_t, no_events = ne)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", code="404 Not Found"), 404

@app.errorhandler(405)
def page_not_found(e):
    return render_template("error.html", code="405 Method Not Allowed"), 405

@app.errorhandler(500)
def page_not_found(e):
    return render_template("error.html", code="500 Internal Server Error"), 500