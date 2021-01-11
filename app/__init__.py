import os
from flask import Flask

# For loading ENV variables in PROD Gunicorn only
# from dotenv import load_dotenv
# load_dotenv('.env')

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

# Import configuration profile based on FLASK_ENV variable - defaults to Production
if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object('config.DevelopmentConfig')
elif os.environ.get('FLASK_ENV') == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.ProductionConfig')


from app.routes import *