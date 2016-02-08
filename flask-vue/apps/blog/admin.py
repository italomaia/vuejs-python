from extensions.admin import admin
from extensions.database import db
from flask_admin.contrib.sqla import ModelView

from .models import Post


class PostView(ModelView):
    pass


admin.add_view(PostView(Post, db.session))
