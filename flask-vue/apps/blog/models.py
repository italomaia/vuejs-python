from extensions import db
import datetime


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    modified = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    title = db.Column(db.Unicode(100))
    slug = db.Column(db.Unicode(100))
    text = db.Column(db.Text)
    tags = db.Column(db.Unicode(60), index=True)

    def __str__(self):
        return self.title
