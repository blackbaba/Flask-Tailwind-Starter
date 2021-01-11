class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    TEST_CONFIG = "production"

class DevelopmentConfig(Config):
    DEBUG = True
    TEST_CONFIG = "development"

class TestingConfig(Config):
    TESTING = True
    TEST_CONFIG = "testing"
