from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    enid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    club = db.Column(db.String(150))
    area = db.Column(db.String(150))
    city = db.Column(db.String(150))
    clubpassword = db.Column(db.String(12))

class umpire(db.Model, UserMixin):
    enid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    award = db.Column(db.String(150))
    area = db.Column(db.String(150))
    city = db.Column(db.String(150))
    umppassword = db.Column(db.String(12))

class match(db.Model, UserMixin):
    match_id = db.Column(db.Integer, primary_key=True)
    match_date = db.Column(db.String(150))
    match_time = db.Column(db.String(150))
    club_name = db.Column(db.String(150))
    area = db.Column(db.String(150))
    city = db.Column(db.String(150))

class confirmation(db.Model, UserMixin):
    confirmation_id = db.Column(db.Integer, primary_key=True)
    match_date = db.Column(db.String(150))
    match_time = db.Column(db.String(150))
    venue = db.Column(db.String(150))
    area = db.Column(db.String(150))
    city = db.Column(db.String(150))
    enid = db.Column(db.Integer, db.ForeignKey('umpire.enid'))
    umpire_name = db.Column(db.String(150))
    confirmed = db.Column(db.Boolean, default=False)
    cancelled = db.Column(db.Boolean, default=False)