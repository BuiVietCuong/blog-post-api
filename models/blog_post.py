from dataclasses import dataclass

from sqlalchemy import Sequence

from db_utils import db

@dataclass
class BlogPost(db.Model):
    id = db.Column(db.Integer, Sequence('b_name', start=1, increment=1), primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    user_email = db.Column(db.Integer, db.ForeignKey('user.email'), unique=False, nullable=False)
    user = db.relationship("User", back_populates="blog_post")

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content
        }