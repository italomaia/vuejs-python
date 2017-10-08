# -*- coding:utf-8 -*-

import os
import sys
from empty import Empty


# apps is a special folder where you can place your blueprints
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_PATH, "apps"))

basestring = getattr(__builtins__, 'basestring', str)


class App(Empty):
    def configure_views(self):
        @self.route("/")
        def index_view():
            return """
        Hello My Friend. This is an example flask view.
        Try creatting blueprints inside ./apps and setting
        them up in your config.py file.""".strip()


def app_factory(config, app_name, blueprints=None):
    # you can use Empty directly if you wish
    app = App(app_name)
    app.configure(config)
    app.add_blueprint_list(blueprints or config.BLUEPRINTS)
    app.setup()

    return app


def heroku():
    import config
    # setup app through APP_CONFIG envvar
    return app_factory(config, config.project_name)
