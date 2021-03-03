import os, sys
import datetime as dt
from flask import (
    render_template,
    url_for,
    redirect,
    request,
    make_response,
    abort,
    jsonify,
    session,
    flash)
from app import app
from app.helpers import *
from app.forms import *
from app.models import *

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# User registration route
@app.route('/register')
def register():
    return render_template('index.html')

# User login route
@app.route('/login')
def login():
    return render_template('index.html')

# 404 Error handler
@app.errorhandler(404)
def resource_not_found(e):
    return render_template('404.html'), 404
