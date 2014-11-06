from gatlin.extensions import db
from gatlin.utils.common import Base
from gatlin.user.models import User
from datetime import datetime
from sqlalchemy import text

import json


# 0 status

class Feed(db.Model,Base):
    __tablename__ = "feeds"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    author = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    feed_type = db.Column(db.Integer)


    def to_dict(self):
        user = User.filter(User.id==self.author).first()
        return {
            "data":json.loads(self.data),
            "author":self.author,
            "username":user.username,
            "feed_type":self.feed_type
        }

    def attr(self,name):
        attrs = json.loads(self.data)
        return attrs.get(name)

class Status(db.Model,Base):

    __tablename__ = "statuses"

    FEED_TYPE = 0

    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.Text)
    author = db.Column(db.Integer)
    created = db.Column(db.DateTime,default=datetime.utcnow())


    def to_dict(self):
        user = User.filter(User.id==self.author).first()
        return {
            "text":self.text,
            "author":self.author,
            "username":user.username,
        }



