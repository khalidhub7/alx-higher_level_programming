#!/usr/bin/python3
"""link class to database_table
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    datab = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(datab)
    session = sessionmaker(bind=datab)()
    first = session.query(State).filter_by(id=1).first()
    try:
        print(first.id, first.name, sep=': ')
    except Exception:
        print("Nothing")
