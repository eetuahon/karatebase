from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.models import Belts, Events
from application.forms import BeltForm

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
  
    return redirect(url_for("belts_index"))

@app.route("/belts/<id>", methods=["POST"])
@login_required
def edit_belts(id):
    return render_template("belts/edit.html", belts = Belts.query.get(id))

#@app.route("/belts/", methods=["POST"])
#@login_required
#def mod_belts(id):
#    form = BeltForm(request.form)
#    belt = form.belt.data
#    if len(belt) == 0:
#        return redirect(url_for("belts_index"))
#    else:
#        b = Belts.query.get(id)
#        b.belt = belt
#        db.session().commit()
#        return redirect(url_for("belts_index"))

@app.route("/belts/del/<id>", methods=["POST"])
@login_required
def belts_del(id):
    b = Belts.query.get(id)

    db.session().delete(b)
    db.session().commit()
  
    return redirect(url_for("belts_index"))