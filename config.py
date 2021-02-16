import os

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jdlfjds7834kjfksdfhdsds'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
