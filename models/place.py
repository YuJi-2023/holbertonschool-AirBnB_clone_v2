#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

"""Build a many to many relationship between place and amenity"""
place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """return the list of Review instances that belong to the place"""
            from models import storage
            review_dict = storage.all(Review)
            review_list = []
            for key, val in review_dict.items():
                if self.id == val.place_id:
                    review_list[key] = val
            return review_list

        @property
        def amenities(self):
            """Return the list of Amenity instances"""
            from models import storage
            amenity_values_list = storage.all(Amenity).values()
            amenity_list = []
            for amenity in amenity_values_list:
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """handles append method for adding an Amenity.id to amenity_ids"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

    else:
        reviews = relationship(
                "Review",
                back_populates='place',
                cascade="all, delete, delete-orphan")

        user = relationship("User", back_populates="places")
        city = relationship("City", back_populates="places")

        amenities = relationship(
                "Amenity", secondary="place_amenity", viewonly=False)
