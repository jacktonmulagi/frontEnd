import os
from os import environ

from flask import config


class Config(object):
    SECRET_KEY = 'key'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.\
        format(user='techmonk', password='techmonk', server='localhost', database='stanbicBank')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    upload_dest = os.path.join(os.getcwd(), 'base/static')
    # list of allowed allowed extensio
    extensions = set(['txt', 'pdf', 'png', 'tiff', 'gtiff'])

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
        environ.get('GENTELELLA_DATABASE_USER', 'techmonk'),
        environ.get('GENTELELLA_DATABASE_PASSWORD', 'techmonk'),
        environ.get('GENTELELLA_DATABASE_HOST', 'localhost'),
        environ.get('GENTELELLA_DATABASE_PORT', 3306),
        environ.get('GENTELELLA_DATABASE_NAME', 'stanbicBank')
    )


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
