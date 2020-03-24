from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, validators

class BeltForm(FlaskForm):
    belt = StringField("Belt / group", [validators.Length(min=3)])
 
    class Meta:
        csrf = False

class SenseiForm(FlaskForm):
    name = StringField("Name")
    logon = StringField("Logon")

    class Meta:
        csrf = False

class TopicForm(FlaskForm):
    desc = StringField("Topic description", [validators.Length(min=3)])

    class Meta:
        csrf = False

class EventForm(FlaskForm):
    name = StringField("Name")
    day = DateTimeField("Day", format='%d.%m.%Y')
    time = StringField("Time")
    info = StringField("Info")

    class Meta:
        csrf = False