import os
basedir = os.path.abspath(os.path.dirname(__file__))  # for setting up database file path

SECRET_KEY = "123ABC987"

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or SECRET_KEY
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False