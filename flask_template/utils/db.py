import sqlalchemy as sa
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker


def create_engine(**connection_params):
    """ Creates an PostgreSQL engine from using options.
    Parameters:
        - host
        - port
        - database
        - username
        - password
        - query
    """
    return sa.create_engine(URL('postgresql', **connection_params))


def get_scoped_session(connection_params):
    engine = create_engine(**connection_params)
    return scoped_session(sessionmaker(bind=engine))
