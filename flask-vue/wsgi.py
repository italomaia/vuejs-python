# coding:utf-8

from main import app_factory
import config

app = app_factory(config, config.project_name)
