#!/usr/bin/python3


"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    class State(State):
        """A class representing a state"""

        def __repr__(self):
            """This function returns the string representation of a state"""
            return f"{self.id}: {self.name}"

    engine = create_engine('mysql+mysqldb://{}:{}@localhost\
            /{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    results = session.query(State).all()
    for result in results:
        print(result)
