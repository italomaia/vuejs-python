from flask import request, jsonify
from flask.views import MethodView

MAX_PER_PAGE = 20
FIRST_PAGE = 1


class Resource(MethodView):
    session = None
    model = None
    schema = None
    schema_cls = None
    pk_param = 'pk'
    pk_type = 'int'

    def __init__(self, session=None, schema_cls=None):
        schema_cls = schema_cls or self.schema_cls
        self.session = session or self.session
        self.schema = schema_cls()
        self.model = schema_cls.Meta.model

    def get_page(self):
        try:
            value = request.args.get('page')
            return FIRST_PAGE if value is None else max(FIRST_PAGE, int(value))
        except ValueError:
            return FIRST_PAGE

    def get_per_page(self):
        try:
            value = request.args.get('per_page')
            return MAX_PER_PAGE \
                if value is None \
                else min(MAX_PER_PAGE, int(value))
        except ValueError:
            return MAX_PER_PAGE

    def get_query(self):
        return self.model.query

    def get_all(self):
        return self.get_query().all()

    def get_one(self, pk):
        return self.get_query().get(pk)

    def get(self, pk=None):
        if pk is None:
            pagination = self.get_query().paginate(
                self.get_page(),
                self.get_per_page()
            )
            return jsonify(dict(
                items=self.schema.dump(
                    pagination.items,
                    many=True
                ).data,
                items_count=len(pagination.items),
                has_next=pagination.has_next,
                has_prev=pagination.has_prev,
                page=pagination.page,
                pages=pagination.pages,
                next_num=pagination.next_num,
                prev_num=pagination.prev_num,
                total=pagination.total
            ))

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
