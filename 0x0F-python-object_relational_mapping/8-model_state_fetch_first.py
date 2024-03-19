from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    results = session.query(State).all()
    if results:
        for i in results:
            if i.id == 1:
                print('{}: {}'.format(i.id, i.name))
    else:
        print('Nothing')
