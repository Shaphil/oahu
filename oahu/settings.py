import os


class Config(object):
    DEBUG = False
    SECRET_KEY = 'my_awesome_super_secret'


basedir = os.path.abspath(os.path.dirname(__file__))


class Development(Config):
    # Application configuration
    DEBUG = True
    DB_NAME = 'oahu.db'
    DB_PATH = os.path.join(basedir, DB_NAME)

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False
