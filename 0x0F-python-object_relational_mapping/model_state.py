#!/usr/bin/python3
""" sqlalchemy practice """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ Define class State inheriting from Base """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True,
    autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
