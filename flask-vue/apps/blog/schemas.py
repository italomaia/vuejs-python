from extensions.schemas import ma
from .models import Post


class PostSchema(ma.Schema):
    class Meta:
        model = Post
