#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import (Column, String, ForeignKey)


class Review(BaseModel, Base):
    """ Review class to store review information

    Attributes:
        place_id:empty(str),it will be the place.id
        user_id:empty(str),it will be the User.id
        test: empty(str)
    """

    __tablename__ = 'reviews'

    if isinstance(models.storage, models.DBStorage):
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    elif isinstance(models.storage, models.FileStorage):
        place_id = ""
        user_id = ""
        text = ""
