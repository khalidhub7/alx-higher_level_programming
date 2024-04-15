#!/usr/bin/python3

""" sql_alchemy """

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ State class """
    __tablename__ = 'states'
    id = Column(
        Integer, autoincrement=True, primary_key=True, 
        nullable=False
        )
    name = Column(
        String(128), nullable=False
    )
