from application import db
from sqlalchemy.sql import text

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

    @staticmethod
    def belts_for_event():
        stmt = text("SELECT B.belt, B.id, E.id FROM Belts B"
                    " LEFT JOIN beltevents BE ON B.id = BE.belt_id"
                    " LEFT JOIN Events E ON E.id = BE.event_id ORDER BY B.belt")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"belt":row[0], "b_id":row[1], "needed_id":row[2]})
        
        return response

    @staticmethod
    def belts_for_event_id(id):
        stmt = text("SELECT B.belt, B.id FROM Belts B"
                    " LEFT JOIN beltevents BE ON B.id = BE.belt_id"
                    " WHERE BE.event_id = :a ORDER BY B.belt").params(a=id)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"belt":row[0], "b_id":row[1]})
        
        return response

    @staticmethod
    def belts_for_event_not_id(id):
        stmt = text("SELECT B.belt, B.id FROM Belts B"
                    " WHERE B.id NOT IN (SELECT Bb.id FROM Belts Bb"
                    " LEFT JOIN beltevents BE ON Bb.id = BE.belt_id"
                    " WHERE BE.event_id = :a) ORDER BY B.belt").params(a=id)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"belt":row[0], "b_id":row[1]})
        
        return response
    
    @staticmethod
    def add_belt(id, b_id):
        stmt = text("INSERT INTO beltevents (belt_id, event_id)"
                    " VALUES (:a, :b)").params(a=b_id, b=id)
        res = db.engine.execute(stmt)

    @staticmethod
    def delete_belt(id, b_id):
        stmt = text("DELETE FROM beltevents"
                    " WHERE belt_id = :a AND event_id = :b").params(a=b_id, b=id)
        res = db.engine.execute(stmt)

    @staticmethod
    def topics_for_event():
        stmt = text("SELECT T.desc, T.id, E.id FROM Topics T"
                    " LEFT JOIN topicevents TE ON T.id = TE.topic_id"
                    " LEFT JOIN Events E ON E.id = TE.event_id ORDER BY T.desc")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"desc":row[0], "t_id":row[1], "needed_id":row[2]})
        
        return response

    @staticmethod
    def topics_for_event_id(id):
        stmt = text("SELECT T.desc, T.id FROM Topics T"
                    " LEFT JOIN topicevents TE ON T.id = TE.topic_id"
                    " WHERE TE.event_id = :a ORDER BY T.desc").params(a=id)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"desc":row[0], "t_id":row[1]})
        
        return response

    @staticmethod
    def topics_for_event_not_id(id):
        stmt = text("SELECT T.desc, T.id FROM Topics T"
                    " WHERE T.id NOT IN (SELECT Tt.id FROM Topics Tt"
                    " LEFT JOIN topicevents TE ON Tt.id = TE.topic_id"
                    " WHERE TE.event_id = :a) ORDER BY T.desc").params(a=id)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"desc":row[0], "t_id":row[1]})
        
        return response
    
    @staticmethod
    def add_topic(id, t_id):
        stmt = text("INSERT INTO topicevents (topic_id, event_id)"
                    " VALUES (:a, :b)").params(a=t_id, b=id)
        res = db.engine.execute(stmt)

    @staticmethod
    def delete_topic(id, t_id):
        stmt = text("DELETE FROM topicevents"
                    " WHERE topic_id = :a AND event_id = :b").params(a=t_id, b=id)
        res = db.engine.execute(stmt)

    staticmethod
    def senseis_for_event():
        stmt = text("SELECT S.name, S.id, E.id FROM Senseis S"
                    " LEFT JOIN senseievents SE ON S.id = SE.sensei_id"
                    " LEFT JOIN Events E ON E.id = SE.event_id ORDER BY S.name")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"name":row[0], "s_id":row[1], "needed_id":row[2]})
        
        return response

    @staticmethod
    def senseis_for_event_id(id):
        stmt = text("SELECT S.name, S.id FROM Senseis S"
                    " LEFT JOIN senseievents SE ON S.id = SE.sensei_id"
                    " WHERE SE.event_id = :a ORDER BY S.name").params(a=id)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"name":row[0], "s_id":row[1]})
        
        return response

    @staticmethod
    def senseis_for_event_not_id(id):
        stmt = text("SELECT S.name, S.id FROM Senseis S"
                    " WHERE S.id NOT IN (SELECT Ss.id FROM Senseis Ss"
                    " LEFT JOIN senseievents SE ON Ss.id = SE.sensei_id"
                    " WHERE SE.event_id = :a) ORDER BY S.name").params(a=id)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"name":row[0], "s_id":row[1]})
        
        return response
    
    @staticmethod
    def add_sensei(id, s_id):
        stmt = text("INSERT INTO senseievents (sensei_id, event_id)"
                    " VALUES (:a, :b)").params(a=s_id, b=id)
        res = db.engine.execute(stmt)

    @staticmethod
    def delete_sensei(id, s_id):
        stmt = text("DELETE FROM senseievents"
                    " WHERE sensei_id = :a AND event_id = :b").params(a=s_id, b=id)
        res = db.engine.execute(stmt)

    @staticmethod
    def events_without_topic():
        stmt = text("SELECT E.day, E.time, E.id"
                    " FROM Events E LEFT JOIN topicevents TE ON"
                    " E.id = TE.event_id GROUP BY E.name having COUNT(TE.topic_id) = 0 ORDER BY E.day, E.time")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"day":row[0], "time":row[1], "id":row[2]})
        
        return response

    @staticmethod
    def belts_without_event():
        stmt = text("SELECT B.belt FROM Belts B LEFT JOIN"
                    " beltevents BE ON B.id = BE.belt_id GROUP BY B.belt"
                    " having COUNT(BE.event_id) = 0 ORDER BY B.belt")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"belt":row[0]})
        
        return response