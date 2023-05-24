#!/usr/bin/python3
"""
    Place Module for HBNB project
"""

import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models import storage_type


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
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
        reviews = relationship("Review", backref="places",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """return reviews associated with a place
            """
            from models import storage
            reviews = storage.all('Review')
            return [review for review in reviews.values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """return a list of amenities
            """
            from model import storage
            amenities = storage.all("Amenities")
            return [amenity for amenity in amenities.values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """ add new amenity to amenities associated with a place
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
        amenity_ids = []


"""place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
               primary_key=True, nullable=False))
"""
