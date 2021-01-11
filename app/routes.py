import os, sys
import datetime as dt
from flask import render_template, url_for, redirect
from app import app
from app.helpers import *
from app.forms import *
from app.models import *

# Home route
@app.route('/')
def index():
    name = "Test User"
    return render_template('index.html', name = name)

# url_for helper function demonstration
@app.route('/url_helper', methods=['GET', 'POST'])
def url_helper():
    return f"{url_for('index')} is root url and {url_for('static', filename='dist/css/main.css')} is url for the main css file"

# Route with a variable
@app.route('/user/<string:username>/posts/<int:post_id>')
def user_posts(username, post_id):
    return f"Post {post_id} for user {username}"

@app.route('/system')
def system():
    return f"NODE ENV: {os.environ.get('NODE_ENV')},  FLASK ENV: {os.environ.get('FLASK_ENV')} and Configuration profile for: {app.config.get('TEST_CONFIG')}"
