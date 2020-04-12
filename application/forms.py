from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, validators

class BeltForm(FlaskForm):
    belt = StringField("Belt / group", [validators.Length(min=3, max=15)])
 
    class Meta:
        csrf = False

class SenseiForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3, max=15)])
    logon = StringField("Logon", [validators.Length(min=3, max=15)])

    class Meta:
        csrf = False

class TopicForm(FlaskForm):
    desc = StringField("Topic description", [validators.Length(min=3, max=30)])

    class Meta:
        csrf = False

class EventForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3, max=15)])
    day = DateTimeField("Day", format='%d.%m.%Y')
    time = StringField("Time", [validators.Length(min=3, max=15)])
    info = StringField("Info")

    class Meta:
        csrf = False