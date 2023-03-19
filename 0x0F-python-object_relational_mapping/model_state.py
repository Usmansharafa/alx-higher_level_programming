#!/usr/bin/python3
"""This modeule defines a class that represents a state"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """A class representing a state

    __tablename__ (str): Table name
    id (sqlalchemy.Integer): State's id
    name (sqlalchemy.String): State's name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
