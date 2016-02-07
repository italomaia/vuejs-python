from .database import db
from .api import api as rest_api
from .schemas import ma
from .webassets import assets
from flask_admin import Admin
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension()
admin = Admin(name='VueJS blog', template_mode='bootstrap3')
