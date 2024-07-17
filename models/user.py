from sqlalchemy import Sequence

from db_utils import db


class User(db.Model):
    email = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String)
    blog_post = db.relationship('BlogPost', back_populates='user', lazy='dynamic')
