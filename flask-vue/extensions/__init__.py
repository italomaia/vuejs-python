from .database import db
from .api import api as rest_api
from .schemas import ma
from .webassets import assets
from .admin import admin
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension()
