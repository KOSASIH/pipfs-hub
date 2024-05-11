# web/middlewares.py
from flask import request


@app.before_request
def log_request():
    logging.info(f"Request received:{request.method} {request.url}")
