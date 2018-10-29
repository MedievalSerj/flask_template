from os import getenv

from flask import Flask
from werkzeug.exceptions import HTTPException

from flask_template.resources.v1.city.resource import city_blueprint
from flask_template.utils.db import get_scoped_session
from flask_template.utils.error_handling import http_error_handler


class App(Flask):

    def __init__(self, *args, session=None, **kwargs):
        self._Session = session
        super().__init__(*args, **kwargs)

    @property
    def db_session(self):
        return self._Session()

    def set_db_session(self, scoped_session):
        self._Session = scoped_session

    def remove_db_session(self):
        self._Session.remove()


def configure_app(app: Flask):
    env = getenv('ENV', 'development').lower().capitalize()
    app.config.from_object('flask_template.config.{}Config'.format(env))


def create_app():
    app = App(__name__)
    configure_app(app)
    app.set_db_session(get_scoped_session(app.config['DB']))
    app.register_blueprint(city_blueprint)
    app.errorhandler(HTTPException)(http_error_handler)
    return app


app = create_app()


@app.teardown_appcontext
def remove_session(response):
    app.remove_db_session()
    return response
