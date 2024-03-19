#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

if __name__ == "__main__":
    datab = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(argv[1], argv[2], argv[3]))
    engine = create_engine(datab)
    ss = sessionmaker(bind=engine)
    first = ss.query(State).filter_by(id=1).first()
    try:
        print(first.id, first.name, sep=': ')
    except Exception:
        print("Nothing")
