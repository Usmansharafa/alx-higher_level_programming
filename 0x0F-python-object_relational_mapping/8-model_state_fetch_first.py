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

    param = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(param, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()
    result = session.query(State).first()
    if not result:
        print("Nothing")
    else:
        print(result)
