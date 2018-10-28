from flask import jsonify
from werkzeug.exceptions import HTTPException


def http_error_handler(error: HTTPException):
    return jsonify({
        'code': error.code,
        'description': error.description
    })
