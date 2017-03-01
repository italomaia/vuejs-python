# coding:utf-8

from main import app_factory
from config import cmm

app = app_factory(cmm, cmm.project_name)
