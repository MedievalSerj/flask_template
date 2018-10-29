from flask import Blueprint, current_app, jsonify
from webargs.flaskparser import use_kwargs
from werkzeug.exceptions import Conflict

from flask_template.marshalling.v1.city.schema import CitySchema
from flask_template.services.exceptions import RecordExistsException
from flask_template.services.v1 import city

city_blueprint = Blueprint('public_city_api', __name__, url_prefix='/v1')


@city_blueprint.route('/city', methods=['GET', ])
def get_all_cities():
    cities = city.get_all_cities(current_app.db_session)
    return jsonify(CitySchema().dump(cities, many=True))


@city_blueprint.route('/city', methods=['POST', ])
@use_kwargs(CitySchema(), locations=('json', ))
def add_city(name):
    try:
        new_city = city.add_city(name, current_app.db_session)
    except RecordExistsException as e:
        raise Conflict(description=e.description)
    return jsonify(CitySchema().dump(new_city))
