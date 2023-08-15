#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns the list of City instances"""
            from models import storage
            city_list = []
            city_dict = storage.all(City)

            for city_obj in city_dict.values():
                if self.id == city_obj.state_id:
                    city_list.append(city_obj)
            return city_list
    else:
        cities = relationship("City",
                              back_populates="state",
                              cascade="all, delete, delete-orphan")
