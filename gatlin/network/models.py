from gatlin.extensions import db
from datetime import datetime



class Feed(db.Model):
    __tablename__ = "feeds"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    author = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    feed_type = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


class Status(db.Model):

    __tablename__ = "statuses"

    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.Text)
    author = db.Column(db.Integer)
    created = db.Column(db.DateTime,default=datetime.utcnow())

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


