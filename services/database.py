# services/database.py
from sqlalchemy import create_engine

class Database:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)

    def execute(self, query):
        # ...
