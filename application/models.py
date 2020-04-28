from application import db
from sqlalchemy.sql import text
import datetime

beltevents = db.Table('beltevents',
    db.Column('belt_id', db.Integer, db.ForeignKey('belts.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True)
)

topicevents = db.Table('topicevents',
    db.Column('topic_id', db.Integer, db.ForeignKey('topics.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True)
)

senseievents = db.Table('senseievents',
    db.Column('sensei_id', db.Integer, db.ForeignKey('senseis.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True)
)
