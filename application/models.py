from application import db

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

class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.Text, unique=True, nullable=True)

    def __init__(self, desc):
        self.desc = desc

class Belts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    belt = db.Column(db.Text, unique=True, nullable=True)

    def __init__(self, belt):
        self.belt = belt

class Senseis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=True)
    logon = db.Column(db.Text, unique=True, nullable=True)

    def __init__(self, name, logon):
        self.name = name
        self.logon = logon

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=True)
    day = db.Column(db.Text, nullable=True)
    #day = db.Column(db.DateTime, nullable=True)
    time = db.Column(db.Text, nullable=True)
    info = db.Column(db.Text, nullable=True)

    belts = db.relationship('Belts', secondary=beltevents, lazy='subquery',
        backref=db.backref('Events', lazy=True))
    topics = db.relationship('Topics', secondary=topicevents, lazy='subquery',
        backref=db.backref('Events', lazy=True))
    senseis = db.relationship('Senseis', secondary=senseievents, lazy='subquery',
        backref=db.backref('Events', lazy=True))

    def __init__(self, name, day, time, info):
        self.name = name
        self.day = day
        self.time = time
        self.info = info
