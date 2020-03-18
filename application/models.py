from application import db

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
    name = db.Column(db.Text, unique=True, nullable=True)
    logon = db.Column(db.Text, unique=True, nullable=True)

    def __init__(self, name, logon):
        self.name = name
        self.logon = logon

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=True)
    day = db.Column(db.Text, nullable=True)
    time = db.Column(db.Text, nullable=True)
    info = db.Column(db.Text, nullable=True)

    def __init__(self, name, day, time, info):
        self.name = name
        self.day = day
        self.time = time
        self.info = info