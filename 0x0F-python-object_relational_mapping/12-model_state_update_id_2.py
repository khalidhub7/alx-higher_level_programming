#!/usr/bin/python3

"""sql_alchemy"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sys import argv

    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(bind=engine)
    sess = Session(bind=engine)

    obj = sess.query(State).filter(State.id == 2).all()
    obj.name = 'New Mexico'
    sess.commit()
