from flask import Flask

# For loading ENV variables in PROD Gunicorn only
# from dotenv import load_dotenv
# load_dotenv('.env')

app = Flask(__name__)
app.config.from_pyfile('settings.py') # load app configuration

from app.routes import *