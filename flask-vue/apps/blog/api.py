from extensions import rest_api, ma, db
from flask_restful import Resource
from flask import request, abort
from blog.models import Post


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post


post_schema = PostSchema()


class ModelResource(Resource):
    db = None
    model = None
    schema = None
    schema_cls = None

    @property
    def session(self):
        return self.db.session

    def __init__(self, db):
        self.db = db
        self.model = self.schema_cls.Meta.model
        self.schema = self.schema_cls()

    def get_query(self):
        return self.model.query

    def get(self, pk=None):
        qs = self.get_query()

        if pk is None:
            return qs.all()

        return qs.get(pk)

    def put(self, pk):
        instance = self.get_query().get(pk)
        errors = self.schema.validate(request.form)

        if errors:
            return errors, 400

        for key, value in self.schema.load(request.form):
            setattr(instance, key, value)

        self.session.add(instance)
        self.session.commit()
        return self.schema.dump(instance)

    def post(self):
        errors = self.schema.validate(request.form)

        if errors:
            return errors, 400

        data = self.schema.load(request.form)
        instance = self.model(**data)
        self.db.session.add(instance)
        self.db.session.commit()
        return self.schema.dump(instance)

    def delete(self, pk):
        query = self.get_query()
        instance = query.get(pk)

        self.session.delete(instance)
        self.session.commit()
        return self.schema.dump(instance)


class PostResource(ModelResource):
    schema_cls = PostSchema


rest_api.add_resource(PostResource, '/posts', resource_class_args=[db])
