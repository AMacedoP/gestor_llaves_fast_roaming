import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

