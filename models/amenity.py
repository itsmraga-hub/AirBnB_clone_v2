#!/usr/bin/python3
""" Amneity Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models import storage_type


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary='place_amenity',
                                       overlaps="amenities")
    else:
        name = ""
