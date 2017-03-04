from extensions.database import db
from sqlalchemy import event

from slugify import slugify

import mistune
import datetime


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    modified = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    title = db.Column(db.Unicode(100))
    slug = db.Column(db.Unicode(100))
    text = db.Column(db.Text)
    html = db.Column(db.Text)
    tags = db.Column(db.Unicode(60), index=True)

    def __str__(self):  # noqa: D105
        return self.title


@event.listens_for(Post.title, 'set')
def post_on_title_set(target, value, oldvalue, initiator):
    target.slug = slugify(value)


# as we don't want the html to be edited manually
# the html has to be generated for each row update
@event.listens_for(Post.text, 'set')
def post_on_text_set(target, value, oldvalue, initiator):
    target.html = mistune.markdown(value)
