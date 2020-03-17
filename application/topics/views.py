from application import app, db
from flask import redirect, render_template, request, url_for
from application.models import Topics

@app.route("/topics", methods=["GET"])
def topics_index():
    return render_template("topics/list.html", topics = Topics.query.all())

@app.route("/topics/new/")
def topics_form():
    return render_template("topics/new.html")

@app.route("/topics/", methods=["POST"])
def topics_create():
    t = Topics(request.form.get("desc"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("topics_index"))

@app.route("/topics/<id>", methods=["POST"])
def edit_topics(id):
    return render_template("topics/edit.html", topics = Topics.query.get(id))

@app.route("/topics/", methods=["POST"])
def mod_topics():
    descr = request.form.get("desc")
    id = request.form.get("id")
    if not desc:
        return redirect(url_for("topics_index"))
    else:
        t = Topics.form.get(id)
        #t.descr = desc
        settattr(t, 'desc', descr)
        db.session().commit()
        return redirect(url_for("topics_index"))