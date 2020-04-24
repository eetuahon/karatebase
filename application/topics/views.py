from application import app, db
from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required
from application.models import Topics, Events
from application.forms import TopicForm
import datetime

@app.route("/topics", methods=["GET"])
def topics_index():
    return render_template("topics/list.html", topics = Topics.query.order_by(Topics.desc).all())

@app.route("/topics/<id>/events", methods=["GET"])
def list_topic_events(id):
    topic = Topics.query.get(id)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    e = Events.query.order_by(Events.day, Events.time).filter(Events.topics.contains(topic), Events.day >= today).all()
    for ev in e:
        date_obj = datetime.datetime.strptime(ev.day, "%Y-%m-%d")
        ev.day = date_obj.strftime("%a %d.%m.%Y")
    return render_template("topics/events_for_topic.html", events = e, Topic = topic)

@app.route("/topics/new/")
@login_required
def topics_form():
    return render_template("topics/new.html", form = TopicForm())

@app.route("/topics/", methods=["POST"])
@login_required
def topics_create():
    form = TopicForm(request.form)
    prior_topic = Topics.query.filter_by(desc=form.desc.data.lower().rstrip()).first()

    if not form.validate():
        return render_template("topics/new.html", form = form)
    elif len(form.desc.data.strip()) < 3:
        form.desc.errors.append("Blanks don't count, have at least 3 char")
        return render_template("topics/new.html", form = form)
    elif prior_topic:
        form.desc.errors.append("Such topic description already exists")
        return render_template("topics/new.html", form = form)

    t = Topics(form.desc.data.lower().rstrip())
    db.session().add(t)
    db.session().commit()
    flash("Master {} to earn black belt, topic added".format(t.desc))
    return redirect(url_for("topics_index"))

@app.route("/topics/<id>", methods=["POST"])
@login_required
def edit_topics(id):
    return render_template("topics/edit.html", topics = Topics.query.get(id))

@app.route("/topics/ed/<id>", methods=["POST"])
@login_required
def mod_topics(id):
    form = TopicForm(request.form)
    descr = form.desc.data.lower().rstrip()
    t = Topics.query.get(id)
    prior_topic = Topics.query.filter_by(desc=form.desc.data.lower().rstrip()).first()
    same = (t == prior_topic)
    if len(descr) == 0:
        return redirect(url_for("topics_index"))
    elif not form.validate():
        return render_template("topics/edit.html", topics = Topics.query.get(id), error = "Topic description should be between 3 and 30 char")
    elif len(form.desc.data.strip()) < 3:
        return render_template("topics/edit.html", topics = Topics.query.get(id), error = "Blanks don't count!")
    elif prior_topic and not same:
        return render_template("topics/edit.html", topics = Topics.query.get(id), error = "Such topic description already exists")
    else:
        t.desc = descr
        db.session().commit()
        flash("Topic {} was modified".format(t.desc))
        return redirect(url_for("topics_index"))

@app.route("/topics/del/<id>", methods=["POST", "GET"])
@login_required
def topics_del(id):
    t = Topics.query.get(id)

    if request.method == "GET":
        return render_template("topics/delete_confirmation.html", topics = t)

    flash("{} is no longer needed for the black belt".format(t.desc).capitalize())
    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("topics_index"))