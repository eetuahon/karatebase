from application import app, db
from flask import redirect, render_template, request, url_for
from application.models import Topics
from application.forms import TopicForm

@app.route("/topics", methods=["GET"])
def topics_index():
    return render_template("topics/list.html", topics = Topics.query.all())

@app.route("/topics/new/")
def topics_form():
    return render_template("topics/new.html", form = TopicForm())

@app.route("/topics/", methods=["POST"])
def topics_create():
    form = TopicForm(request.form)

    if not form.validate():
        return render_template("topics/new.html", form = form)

    t = Topics(form.desc.data.lower())
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("topics_index"))

@app.route("/topics/<id>", methods=["POST"])
def edit_topics(id):
    return render_template("topics/edit.html", topics = Topics.query.get(id))

@app.route("/topics/ed/<id>", methods=["POST"])
def mod_topics(id):
    form = TopicForm(request.form)
    descr = form.desc.data.lower()
    if len(descr) == 0:
        return redirect(url_for("topics_index"))
    else:
        t = Topics.query.get(id)
        t.desc = descr
        db.session().commit()
        return redirect(url_for("topics_index"))

@app.route("/topics/del/<id>", methods=["POST"])
def topics_del(id):
    t = Topics.query.get(id)

    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("topics_index"))