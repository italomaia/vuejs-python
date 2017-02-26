from flask import Blueprint

app = Blueprint(
    'blog', __name__,
    template_folder='templates',
    static_folder='static'
)
