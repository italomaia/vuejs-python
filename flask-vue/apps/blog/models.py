from extensions.database import db
from flask_sqlalchemy import before_models_committed

import mistune
import datetime


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    modified = db.Column(db.DateTime)
    title = db.Column(db.Unicode(100))
    slug = db.Column(db.Unicode(100))
    text = db.Column(db.Text)
    html = db.Column(db.Text)
    tags = db.Column(db.Unicode(60), index=True)

    def __str__(self):
        return self.title

    @classmethod
    def before_commit(sender, app, changes):
        for model, change in changes:
            if isinstance(model, Post) and change in ('insert', 'update'):
                # onupdate for field is only called if field is in the SET
                # this makes sure it is always called
                model.modified = datetime.datetime.utcnow()

                # as we don't want the html to be edited manually
                # the html has to be generated for each row update
                model.html = mistune.markdown(model.text)


before_models_committed.connect(Post.before_commit)
