#!/usr/bin/python3

"""sql_alchemy"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """ cities class """
    __tablename__ = 'cities'
    Base.super(id, name)
    state_id = Column(
        Integer, ForeignKey('states.id'), nullable=False
        )
