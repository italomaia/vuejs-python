from extensions.socketio import socketio
from flask_sqlalchemy import models_committed
from .schemas import PostSchema
from .models import Post

namespace = '/blog/io'
post_schema = PostSchema()


def post_after_commit(sender, changes):
    for model, change in changes:
        if isinstance(model, Post) and change in ('insert',):
            emit_new_posts()
            break


def emit_new_posts():
    socketio.emit('new posts', namespace=namespace)


models_committed.connect(post_after_commit)
