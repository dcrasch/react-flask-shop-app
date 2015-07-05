import os

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

    PROJECT = "shop_app"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(
        os.path.dirname(__file__)
    ))
    LOG_FOLDER = os.path.join(PROJECT_ROOT, 'logs')
    if not os.path.exists(LOG_FOLDER):
        os.mkdir(LOG_FOLDER)

class DefaultConfig(Config):
    DEBUG=True

class DevelopmentConfig(DefaultConfig):
    pass

