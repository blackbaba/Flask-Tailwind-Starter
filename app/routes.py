import os, sys
import datetime as dt
from flask import render_template, url_for
from app import app
from app.helpers import *
from app.forms import *
from app.models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/system')
def system():
    return f"NODE ENV: {os.environ.get('NODE_ENV')},  FLASK ENV: {os.environ.get('FLASK_ENV')} and Configuration profile for: {app.config.get('TEST_CONFIG')}"
