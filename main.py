# main.py
from flask import Flask, request, jsonify
import logging
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

logging.basicConfig(level=logging.INFO)

@app.route('/api/pipfs', methods=['GET'])
def get_pipfs():
    # ...
