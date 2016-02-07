from extensions import admin, db
from flask_admin.contrib.sqla import ModelView

from .models import *


class PostView(ModelView):
    pass


admin.add_view(PostView(Post, db.session))
