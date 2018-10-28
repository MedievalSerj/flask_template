from os import getenv


class Config:
    HOST = getenv('HOST', '0.0.0.0')
    PORT = getenv('PORT', 8080)
    SECRET_KEY = getenv('SECRET_KEY', 'its-dangerous!')
    DB = {
        'username': getenv('DB_USER'),
        'password': getenv('DB_PASSWORD'),
        'host': getenv('DB_HOST'),
        'port': getenv('DB_PORT'),
        'database': getenv('DB_DATABASE')
    }
    REQUEST_LIFETIME = 30


class DevelopmentConfig(Config):
    DEBUG = True
    REQUEST_LIFETIME = 0
