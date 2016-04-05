from extensions.api import rest_api
from extensions.schemas import ma
from extensions.database import db
from utils.api import ModelResource
from blog.models import Post


class PostSchema(ma.Schema):
    class Meta:
        model = Post


class PostResource(ModelResource):
    session = db.session
    schema_cls = PostSchema


rest_api.add_resource(PostResource, '/posts', endpoint='api.posts')
