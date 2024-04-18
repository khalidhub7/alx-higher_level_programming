#!/usr/bin/python3

"""sql_alchemy"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """ cities class """
    id = Column(
        Integer, autoinrement=True, primary_key=True, nullable=False
    )
    name = Column(
        String(128), nullable=False
        )
    state_id = Column(
        Integer, ForeignKey('states.id'), nullable=False
    )
