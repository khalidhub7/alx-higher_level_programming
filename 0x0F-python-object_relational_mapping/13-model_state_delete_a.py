#!/usr/bin/python3

"""sql_alchemy"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sys import argv

    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(bind=engine)
    sess = Session(bind=engine)

    sess.query(State).filter(State.name.like('%a%')).delete()
    sess.commit()

    result = sess.query(State).all()
    for j in result:
        print('{}: {}'.format(j.id, j.name))
