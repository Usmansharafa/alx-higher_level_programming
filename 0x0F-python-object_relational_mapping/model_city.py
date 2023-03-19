#!/usr/bin/python3
"""This modeule defines a class that represents a city"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State


Base = declarative_base()


class City(Base):
    """A class representing a city

    __tablename__ (str): Table name
    id (sqlalchemy.Integer): City's id
    name (sqlalchemy.String): City's name
    state_id (sqlalchemy.Integer): Corresponding state id
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
