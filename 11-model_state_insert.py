#!/usr/bin/python3


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True  
    )

    
    Session = sessionmaker(bind=engine)

    
    my_session = Session()

    state = State(name="Louisiana")
    my_session.add(state)
    my_session.commit()
    print(state.id)
    
    my_session.close()