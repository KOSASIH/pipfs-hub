# utils/utils.py
import hashlib


def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()
