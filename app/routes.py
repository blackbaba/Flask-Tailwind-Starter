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

