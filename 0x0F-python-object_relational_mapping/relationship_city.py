#!/usr/bin/python3

"""sql_alchemy"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """ cities class """
    __tablename__ = 'cities'
    id = Column(
        Integer, autoincrement=True, primary_key=True, nullable=False
    )
    name = Column(
        String(128), nullable=False
        )
    state_id = Column(
        Integer, ForeignKey('states.id'), nullable=False
    )
