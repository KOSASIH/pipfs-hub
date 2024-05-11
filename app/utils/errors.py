# Error handling utilities
from flask import abort


def not_found(message):
    abort(404, message=message)
