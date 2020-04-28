from application import db
from sqlalchemy.sql import text
import datetime

class Senseis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=True)
    logon = db.Column(db.Text, unique=True, nullable=True)

    def __init__(self, name, logon):
        self.name = name
        self.logon = logon

    def count_senseievents(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        stmt = text("SELECT COUNT(SE.event_id) FROM Senseievents SE LEFT JOIN"
                    " Events E ON SE.event_id = E.id WHERE SE.sensei_id = :a"
                    " AND E.day >= :b").params(a=self.id, b=today)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append(row[0])
        
        return response[0]