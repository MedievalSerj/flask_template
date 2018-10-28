from sqlalchemy.engine.url import URL


def create_db_url(app):
    return URL(
        'postgresql',
        username=app.config['DB']['username'],
        password=app.config['DB']['password'],
        host=app.config['DB']['host'],
        port=app.config['DB']['port'],
        database=app.config['DB']['database'],
    )
