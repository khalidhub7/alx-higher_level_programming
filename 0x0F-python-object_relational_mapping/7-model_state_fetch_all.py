#!/usr/bin/python3
""" lists all State using sql alchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    datab_url = "mysql://{}:{}@localhost/{}" \
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    enginee = create_engine(datab_url)
    Session = sessionmaker(bind=enginee)
    sess = Session()
    results = sess.query(State).all()
    for i in results:
        print("{}: {}".format(i.id, i.name))
