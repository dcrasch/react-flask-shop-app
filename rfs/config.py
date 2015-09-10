import os

class BaseConfig(object):
    PROJECT = "rfs"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(
        os.path.dirname(__file__)
    ))

    DEBUG = False
    
    ADMINS = []
    SECRET_KEY = None
    LOG_FOLDER = os.path.join(PROJECT_ROOT, 'logs')
    if not os.path.exists(LOG_FOLDER):
        os.mkdir(LOG_FOLDER)
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'

class DefaultConfig(BaseConfig):
    DEBUG=True
    

class DevelopmentConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_ECHO = False
    SECRET_KEY = os.urandom(24)
    ##ASSETS_DEBUG = True
class TestConfig(DefaultConfig):
    pass

class ProductionConfig(BaseConfig):
    DEBUG = False

