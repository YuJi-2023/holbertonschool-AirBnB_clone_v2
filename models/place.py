#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import os

"""creating relationship table"""
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey("places.id"),
                             nullable=False,
                             primary_key=True),
                      Column('amenity_id',
                             String(60),
                             ForeignKey("amenities.id"),
                             nullable=False,
                             primary_key=True))


class Place(BaseModel, Base):
    """ defines class Place"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    user = relationship("User")
    cities = relationship("City")
    reviews = relationship("Review",
                           back_populates="place",
                           cascade="all, delete, delete-orphan")
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 back_populates="place_amenities", #not in task, chatty suggest
                                 viewonly=False)

    else:
        @property
        def amenities(self):
            """returns the list of Amenity instances"""
            from models import Amenity, storage
            amenities_obj_list = []
            amenities_obj_dict = storage.all(Amenity)

            for amenity_obj in amenities_obj_dict.values():
                if amenity_obj.id in self.amenity_ids:
                    amenities_obj_list.append(amenity_obj)
            return amenities_obj_list

        @amenities.setter
        def amenities(self, value):
            """handles append method for adding an Amenity.id"""
            from models import Amenity, storage
            if type(value) is Amenity:
                self.amenity_ids.append(value.id)
    @property
    def reviews(self):
        """returns the list of Review instances"""
        from models import Review, storage
        review_list = []
        review_dict = storage.all(Review)

        for review_obj in review_dict.values():
            if self.id == review_obj.place_id:
                review_list.append(review_obj)
        return review_list
