from flask import render_template

from . import main


@main.route('/')
def index():
    "About page"
    return render_template("index.html")
