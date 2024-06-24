#!/usr/bin/python3

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True  
    )

    
    Session = sessionmaker(bind=engine)

    
    my_session = Session()

    result = my_session.query(State).filter(State.name == argv[4]).scalar()
    if result is None:
        print("Not found")
    else:
        print("{}".format(result.id))

    
    my_session.close()