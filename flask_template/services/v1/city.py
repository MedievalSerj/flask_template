from flask_template.db.models import City
from ..exceptions import RecordExistsException
from sqlalchemy.exc import IntegrityError


def get_all_cities(session):
    return (session.query(City)
            .order_by(City.name)
            .all())


def add_city(name, session):
    city = City(name=name)
    try:
        session.add(city)
        session.commit()
    except IntegrityError:
        session.rollback()
        raise RecordExistsException(
            description=f"record with name '{name}' already exists")
    return city
