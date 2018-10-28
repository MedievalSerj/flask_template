from flask import Flask
from flask_template.resources.v1.city.resource import city_blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy_session import flask_scoped_session
from os import getenv
from flask_template.utils.db import create_db_url
from flask_template.utils.error_handling import http_error_handler
from werkzeug.exceptions import HTTPException


class App(Flask):

    def __init__(self, *args, session=None, **kwargs):
        self.db_session =session
        super().__init__(*args, **kwargs)


def get_sqlalchemy_session_factory(url):
    engine = create_engine(url)
    return sessionmaker(bind=engine)


def configure_app(app: Flask):
    env = getenv('ENV', 'development').lower().capitalize()
    app.config.from_object('flask_template.config.{}Config'.format(env))


def create_app():
    app = App(__name__)
    configure_app(app)
    app.db_session = flask_scoped_session(
        get_sqlalchemy_session_factory(create_db_url(app)))
    app.register_blueprint(city_blueprint)
    app.errorhandler(HTTPException)(http_error_handler)
    return app


app = create_app()
