# web/models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pipfs(Base):
    __tablename__ = "pipfs"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    # ...
