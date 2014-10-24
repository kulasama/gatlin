from gatlin.extensions import db, cache
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    phone = db.Column(db.String(200),unique=True)
    password = db.Column(db.String(120), nullable=False)
    joined = db.Column(db.DateTime, default=datetime.utcnow())
    lastseen = db.Column(db.DateTime, default=datetime.utcnow())
    birthday = db.Column(db.DateTime)
    gender = db.Column(db.String(10))
    website = db.Column(db.String(200))
    location = db.Column(db.String(100))
    avatar = db.Column(db.String(200))


    def save(self):
        """Saves a user. If a list with groups is provided, it will add those
        to the secondary groups from the user.

        :param groups: A list with groups that should be added to the
                       secondary groups from user.
        """

        db.session.add(self)
        db.session.commit()
        return self

    def set_password(self, raw_password):
        """Generates a password hash for the provided password"""
        self.password = generate_password_hash(raw_password)
