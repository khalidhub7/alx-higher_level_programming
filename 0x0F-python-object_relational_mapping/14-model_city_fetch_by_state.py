#!/usr/bin/python3

"""sql_alchemy"""

if __name__ == '__main__':
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv

    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(bind=engine)
    sess = Session(bind=engine)

    states = sess.query(State).all()
    cities = sess.query(City).all()

    for i in cities:
        for j in states:
            if j.id == i.state_id:
                new = j.name
        print('{}: ({}) {}'.format(new, i.id, i.name))
