# web/errors.py
from flask import jsonify


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404
