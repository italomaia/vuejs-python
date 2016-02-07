from flask_restful import Resource
from flask import request


class ModelResource(Resource):
    session = None
    model = None
    schema = None
    schema_cls = None

    def __init__(self, session=None, schema_cls=None):
        session = session or self.session
        schema_cls = schema_cls or self.schema_cls

        self.session = session
        self.schema_cls = schema_cls
        self.schema = schema_cls()
        self.model = schema_cls.Meta.model

    def get_query(self):
        return self.model.query

    def get_all(self):
        return self.get_query().all()

    def get_one(self, pk):
        return self.get_query().get(pk)

    def get(self, pk=None):
        if pk is None:
            return self.schema.dump(self.get_all(), many=True).data

        return self.schema.dump(self.get_one(pk)).data

    def put(self, pk):
        instance = self.get_one(pk)
        errors = self.schema.validate(request.form)

        if errors:
            return errors, 400

        for key, value in self.schema.load(request.form):
            setattr(instance, key, value)

        self.session.add(instance)
        self.session.commit()
        return self.schema.dump(instance).data

    def post(self):
        errors = self.schema.validate(request.form)

        if errors:
            return errors, 400

        data = self.schema.load(request.form)
        instance = self.model(**data)
        self.db.session.add(instance)
        self.db.session.commit()
        return self.schema.dump(instance).data

    def delete(self, pk):
        instance = self.get_one(pk)

        self.session.delete(instance)
        self.session.commit()
        return self.schema.dump(instance).data

