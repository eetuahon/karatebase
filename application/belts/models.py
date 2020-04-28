from application import db
from sqlalchemy.sql import text
import datetime

class Belts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    belt = db.Column(db.Text, unique=True, nullable=True)

    def __init__(self, belt):
        self.belt = belt

    def count_beltevents(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        stmt = text("SELECT COUNT(BE.event_id) FROM Beltevents BE LEFT JOIN"
                    " Events E ON BE.event_id = E.id WHERE BE.belt_id = :a"
                    " AND E.day >= :b").params(a=self.id, b=today)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append(row[0])
        
        return response[0]

    def count_14d_beltevents(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        week = (datetime.datetime.now() + datetime.timedelta(days=14)).strftime("%Y-%m-%d")
        stmt = text("SELECT COUNT(BE.event_id) FROM Beltevents BE LEFT JOIN"
                    " Events E ON BE.event_id = E.id WHERE BE.belt_id = :a"
                    " AND E.day >= :b AND E.day < :c").params(a=self.id, b=today, c=week)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append(row[0])
        
        return response[0]