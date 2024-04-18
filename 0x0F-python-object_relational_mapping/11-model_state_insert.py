#!/usr/bin/python3

"""sql_alchemy"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sys import argv

    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'\
            .format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(bind=engine)
    new_obj = State(name='Louisiana')

    sess = Session(bind=engine)
    sess.add(new_obj)
    sess.commit()


    """ to display all
    
    new = sess.query(State).all()
    for i in new:
        print('{}: {}'.format(i.id, i.name)) 
    """
    
    new = sess.query(State).filter(State.name == 'Louisiana').all()
    print("{}".format(new[0].id))
