#!/usr/bin/python3
""" sqlalchemy practice """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String


if __name__ == '__main__':
    Base = declarative_base()
    class State(Base):
        """ define class
        State inherite from Base """
        __tablename__ = "states"
        id = Column(Integer, primary_key=True, 
                    autoinrement=True, nullable=False)

        name = Column(String(128), nullable=False)
