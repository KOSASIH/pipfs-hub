# User model
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
