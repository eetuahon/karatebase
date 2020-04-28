from application import db
from sqlalchemy.sql import text
import datetime

class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.Text, unique=True, nullable=True)

    def __init__(self, desc):
        self.desc = desc

    def count_topicevents(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        stmt = text("SELECT COUNT(TE.event_id) FROM Topicevents TE LEFT JOIN"
                    " Events E ON TE.event_id = E.id WHERE TE.topic_id = :a"
                    " AND E.day >= :b").params(a=self.id, b=today)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append(row[0])
        
        return response[0]