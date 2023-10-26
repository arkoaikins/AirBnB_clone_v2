#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import (Column, String)
from sqlalchemy.orm import relationship
import models


class Amenity(BaseModel, Base):
    """
    Different amenities present in a place

    Attribute:
        name: (str)Name of Amenity
    """
    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""
