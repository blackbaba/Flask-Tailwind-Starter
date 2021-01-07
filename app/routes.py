from flask import render_template, url_for
from app import app
from app.helpers import *


@app.route('/')
def index():
    return render_template('index.html')
