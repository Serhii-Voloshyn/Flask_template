import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")\
        or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "sqlite:///./test.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = "http"