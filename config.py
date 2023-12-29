import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TESTING = False
    CSRF_ENABLED = False
    BASE_DIR = basedir


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    ENV = "production"
    DEVELOPMENT = False
    DEBUG = False
