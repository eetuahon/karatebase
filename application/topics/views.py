from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.models import Topics
from application.forms import TopicForm

@app.route("/topics", methods=["GET"])
def topics_index():
    return render_template("topics/list.html", topics = Topics.query.order_by(Topics.desc).all())

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
        form.desc.errors.append("This topic already exists")
        return render_template("topics/new.html", form = form)

    t = Topics(form.desc.data.lower().rstrip())
    if len(t.desc) > 0:
        db.session().add(t)
        db.session().commit()
  
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
        return render_template("topics/edit.html", topics = Topics.query.get(id), error = "This topic already exists")
    else:
        t.desc = descr
        db.session().commit()
        return redirect(url_for("topics_index"))

@app.route("/topics/del/<id>", methods=["POST"])
@login_required
def topics_del(id):
    t = Topics.query.get(id)

    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("topics_index"))