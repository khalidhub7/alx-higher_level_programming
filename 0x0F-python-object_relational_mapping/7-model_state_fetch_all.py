#!/usr/bin/python3

"""sql_alchemy"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import Session

    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'\
            .format(argv[1], argv[2], argv[3])
        )
    Base.metadata.create_all(bind=engine)
    sess = Session(bind=engine)
    result = sess.query(State).order_by(State.id).all()

    for i in result:
        print('{}: {}'.format(i.id, i.name))
