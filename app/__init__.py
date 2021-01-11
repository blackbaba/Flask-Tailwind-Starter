import os
from flask import Flask

# For loading ENV variables in PROD Gunicorn only
# from dotenv import load_dotenv
# load_dotenv('.env')

app = Flask(__name__)
if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
elif os.environ.get('FLASK_ENV') == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

from app.routes import *