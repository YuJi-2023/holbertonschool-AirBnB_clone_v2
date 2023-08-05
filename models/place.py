#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


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
    reviews = relationship("Review", back_populates="place", cascade="all, delete, delete-orphan")

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
