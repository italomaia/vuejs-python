from extensions.schemas import ma
from .models import Post


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post
