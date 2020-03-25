from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.models import Belts
from application.forms import BeltForm

@app.route("/belts", methods=["GET"])
def belts_index():
    return render_template("belts/list.html", belts = Belts.query.order_by(Belts.belt).all())

@app.route("/belts/new/")
@login_required
def belts_form():
    return render_template("belts/new.html", form = BeltForm())

@app.route("/belts/", methods=["POST"])
@login_required
def belts_create():
    form = BeltForm(request.form)

    if not form.validate():
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