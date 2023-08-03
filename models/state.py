#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage
from models import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = states
    name = Coulmn(String(128), nullable=False)
    cites = relationship("City", back_populates="state", cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """returns the list of City instances"""
        city_list = []
        city_dict = storage.all(City)

        city.state_id == State.id
        for k, v in city_dict:
            if State.id in k:
                # v.state_id ????
                city_list.append(v)
        return city_list
