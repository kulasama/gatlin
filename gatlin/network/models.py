from gatlin.extensions import db
from gatlin.user.models import Base
from datetime import datetime


# 0 status

class Feed(db.Model,Base):
    __tablename__ = "feeds"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    author = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    feed_type = db.Column(db.Integer)



class Status(db.Model,Base):

    __tablename__ = "statuses"

    FEED_TYPE = 0

    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.Text)
    author = db.Column(db.Integer)
    created = db.Column(db.DateTime,default=datetime.utcnow())


