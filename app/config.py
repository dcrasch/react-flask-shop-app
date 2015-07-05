class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class DevelopmentConfig(Config):
    DEBUG=True
