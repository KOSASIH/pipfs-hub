# web/config.py
from decouple import config

SECRET_KEY = config("SECRET_KEY")
DATABASE_URI = config("DATABASE_URI")
