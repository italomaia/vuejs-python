from flask import Blueprint
from flask import render_template, flash, redirect, url_for

app = Blueprint('blog', __name__, template_folder='templates')