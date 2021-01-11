import os, sys
import datetime as dt
from flask import render_template, url_for
from app import app
from app.helpers import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/environment')
def environment():
    return f"NODE ENV: {os.environ.get('NODE_ENV')} and FLASK ENV: {os.environ.get('FLASK_ENV')} and Configuration profile for: {app.config.get('TEST_CONFIG')}"
