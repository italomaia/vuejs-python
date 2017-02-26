from flask import render_template
from .bp import app


@app.route("/")
def index():
    return render_template('blog/index.html')
