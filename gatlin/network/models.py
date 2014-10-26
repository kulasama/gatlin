from gatlin.extensions import db


class Feed(db.Model):
    __tablename__ = "feeds"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    author = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.utcnow()))
    feed_type = db.Cloumn(db.Integer)


class Status(db.Model):

    __tablename__ = "statuses"

    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.Text)
    author = db.Column(db.Integer)
    created = db.Column(db.DateTime,default=datatime.utcnow())


