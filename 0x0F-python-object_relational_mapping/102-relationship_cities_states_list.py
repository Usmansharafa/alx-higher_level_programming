#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the DB
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).join(City).order_by(State.id).all()

    for state in st:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")
