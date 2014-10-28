from gatlin.extensions import db




class Base(object):

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def all(cls):
        return db.query(cls).all()