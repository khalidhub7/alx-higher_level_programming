#!/usr/bin/python3

"""sql_alchemy"""

if __name__ == '__main__':
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv

    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(bind=engine)
    sess = Session(bind=engine)
    result = sess.query(State).filter(State.name.like("{}".format(argv[4]))).all()

    if result != []:
        print('{}'.format(result[0].id))
    if result == []:
        print('Not found')
