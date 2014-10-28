from gatlin.extensions import db




class Base(object):

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def filter(cls,*kwargs):
        return db.session.query(cls).filter(*kwargs)


    @classmethod
    def all(cls):
        return db.session.query(cls).all()