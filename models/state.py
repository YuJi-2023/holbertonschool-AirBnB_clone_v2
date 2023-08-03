#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Foreignkey

class State(BaseModel, Base):
    """ State class """
    __tablename__ = states
    name = Coulmn(String(128), nullable=False)
    state_id = relationship(city)
