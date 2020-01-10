from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    #links = db.relationship("ShortUrl", backref="user", lazy=True)

    def __str__(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated


class ShortUrl(db.Model):
    __tablename__ = 'shortenurls'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)
    link = db.Column(db.String, unique=True, nullable=False)
    short_code = db.Column(db.String, unique=True, nullable=False)
    custom_code = db.Column(db.String, unique=True)
