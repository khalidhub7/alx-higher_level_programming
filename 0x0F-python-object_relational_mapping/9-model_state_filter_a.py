#!/usr/bin/python3
"""link class to database_table with some filter
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
    results = session.query(State).filter(State.name.like('%a%'))
    for i in results:
        print('{}: {}'.format(i.id, i.name))
