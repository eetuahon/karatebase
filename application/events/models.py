from application import db
from sqlalchemy.sql import text
import datetime
from application.models import beltevents, topicevents, senseievents

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=True)
    day = db.Column(db.Text, nullable=True)
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

    def belt_list(self):
        stmt = text("SELECT B.belt, B.id FROM Belts B"
                    " LEFT JOIN beltevents BE ON B.id = BE.belt_id"
                    " WHERE BE.event_id = :a ORDER BY LOWER(B.belt)").params(a=self.id)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"belt":row[0], "b_id":row[1]})
        
        return response

    def non_belt_list(self):
        stmt = text("SELECT B.belt, B.id FROM Belts B"
                    " WHERE B.id NOT IN (SELECT Bb.id FROM Belts Bb"
                    " LEFT JOIN beltevents BE ON Bb.id = BE.belt_id"
                    " WHERE BE.event_id = :a) ORDER BY LOWER(B.belt)").params(a=self.id)
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

    def topic_list(self):
        stmt = text("SELECT T.desc, T.id FROM Topics T"
                    " LEFT JOIN topicevents TE ON T.id = TE.topic_id"
                    " WHERE TE.event_id = :a ORDER BY LOWER(T.desc)").params(a=self.id)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"desc":row[0], "t_id":row[1]})
        
        return response

    def non_topic_list(self):
        stmt = text("SELECT T.desc, T.id FROM Topics T"
                    " WHERE T.id NOT IN (SELECT Tt.id FROM Topics Tt"
                    " LEFT JOIN topicevents TE ON Tt.id = TE.topic_id"
                    " WHERE TE.event_id = :a) ORDER BY LOWER(T.desc)").params(a=self.id)
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

    def sensei_list(self):
        stmt = text("SELECT S.name, S.id FROM Senseis S"
                    " LEFT JOIN senseievents SE ON S.id = SE.sensei_id"
                    " WHERE SE.event_id = :a ORDER BY LOWER(S.name)").params(a=self.id)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"name":row[0], "s_id":row[1]})
        
        return response

    def non_sensei_list(self):
        stmt = text("SELECT S.name, S.id FROM Senseis S"
                    " WHERE S.id NOT IN (SELECT Ss.id FROM Senseis Ss"
                    " LEFT JOIN senseievents SE ON Ss.id = SE.sensei_id"
                    " WHERE SE.event_id = :a) ORDER BY LOWER(S.name)").params(a=self.id)
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
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        stmt = text("SELECT E.day, E.time, E.id, E.name"
                    " FROM Events E LEFT JOIN topicevents TE ON"
                    " E.id = TE.event_id WHERE E.day >= :a GROUP BY E.id, E.day, E.time having"
                    " COUNT(TE.topic_id) = 0 ORDER BY E.day, LOWER(E.time)").params(a=today)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"day":row[0], "time":row[1], "id":row[2], "name":row[3]})
        
        return response

    @staticmethod
    def belts_without_event():
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        stmt = text("SELECT B.belt FROM Belts B WHERE B.id NOT IN (SELECT Belts.id FROM Belts LEFT"
                    " JOIN beltevents BE ON Belts.id = BE.belt_id LEFT JOIN Events E on BE.event_id = E.id"
                    " WHERE E.day >= :a ) ORDER BY B.belt").params(a=today)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"belt":row[0]})
        
        return response