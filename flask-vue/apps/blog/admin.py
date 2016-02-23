from extensions.admin import admin
from extensions.database import db
from flask_admin.contrib.sqla import ModelView

from .models import Post
from .forms import PostForm


class PostView(ModelView):
    def get_form(self):
        return PostForm


admin.add_view(PostView(Post, db.session))
