import os
import logging
from datetime import timedelta

project_name = os.getenv('PROJECT')


# base config class; extend it to your needs.
# use DEBUG mode?
DEBUG = os.getenv('FLASK_DEBUG') == '1'
DEBUG_TB_INTERCEPT_REDIRECTS = False

SERVER_NAME = os.getenv("SERVER_NAME")

# use TESTING mode?
TESTING = os.getenv('FLASK_TESTING') == '1'

# use server x-sendfile?
USE_X_SENDFILE = os.getenv('FLASK_USE_X_SENDFILE') == '1'

# DATABASE CONFIGURATION
# see http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO') == '1'
SQLALCHEMY_TRACK_MODIFICATIONS = not DEBUG

WTF_CSRF_ENABLED = os.getenv('FLASK_WTF_CSRF_ENABLED') == '1'
SECRET_KEY = os.getenv('FLASK_SECRET', 'secret')  # import os; os.urandom(24)

# LOGGING
LOGGER_NAME = "%s_log" % project_name
LOG_FILENAME = "/var/tmp/app.%s.log" % project_name
LOG_LEVEL = logging.INFO
# used by logging.Formatter
LOG_FORMAT = "%(asctime)s %(levelname)s\t: %(message)s"

PERMANENT_SESSION_LIFETIME = timedelta(days=7)

# EMAIL CONFIGURATION
MAIL_SERVER = "localhost"
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_DEBUG = False
MAIL_USERNAME = None
MAIL_PASSWORD = None
DEFAULT_MAIL_SENDER = "example@%s.com" % project_name

EXTENSIONS = [
    'extensions.debug.toolbar',
    'extensions.database.db',
    'extensions.database.migrate',
    'extensions.schemas.ma',
    'extensions.socketio.socketio',
    'extensions.admin.admin',
]

LOAD_MODULES_EXTENSIONS = [
    'api',
    'admin',
    'views',
    'models',
    'socket',
]

# see example/ for reference
# where app is a Blueprint instance
#
# Examples:
# BLUEPRINTS = ['blog']  # where app is a Blueprint instance
# BLUEPRINTS = [('blog', {'url_prefix': '/myblog'})]
BLUEPRINTS = []
