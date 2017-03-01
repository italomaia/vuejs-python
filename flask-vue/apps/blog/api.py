from extensions.schemas import ma
from extensions.database import db
from utils.api import Resource
from blog.models import Post
from .bp import app


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post


class PostResource(Resource):
    session = db.session
    schema_cls = PostSchema


post_api = PostResource.as_view('post_api')
app.add_url_rule(
    '/posts',
    view_func=post_api,
    methods=['GET', 'POST']
)
app.add_url_rule(
    '/posts/<int:pk>',
    view_func=post_api,
    methods=['GET', 'PUT', 'DELETE']
)
