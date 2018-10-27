import multiprocessing
from os import getenv


from gunicorn.http import wsgi


class Response(wsgi.Response):
    def default_headers(self, *args, **kwargs):
        allowed_headers = ('Authorization, Unix-Timestamp, Content-Type')
        return [*super().default_headers(*args, **kwargs),
                f'Access-Control-Allow-Headers: {allowed_headers}\r\n',
                'Access-Control-Allow-Origin: *\r\n']


wsgi.Response = Response

# bind adrress
bind = getenv('GUNICORN_BIND', '0.0.0.0:8080')
forwarded_allow_ips = '*'

# reload workers on code change (usefull for development)
reload = bool(getenv('GUNICORN_RELOAD', False))

# logging
accesslog = '-'
errorlog = '-'
loglevel = getenv('GUNICORN_LOGLEVEL', 'info')

# timeout
timeout = getenv('GUNICORN_TIMEOUT', 600)

# number of workers
workers = getenv('GUNICORN_WORKERS', multiprocessing.cpu_count() * 2 + 1)
