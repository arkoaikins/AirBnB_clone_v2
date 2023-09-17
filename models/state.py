#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import (Column, String)
from sqlalchemy.orm import (relationship)
from models import DBStorage
from models import FileStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # Relationship
    if isinstance(models.storage, DBStorage):
        cities = relationship('City', backref='state',
                              cascade="all, delete, delete-orphan")
    elif isinstance(models.storage, FileStorage):
        @property
        def cities(self):
            """
            Return a list of 'City' instances with state_id equal to
            self.id
            """
            objs = list()
            if objs is None:
                return list()

            for obj in models.storage.all(City):
                if objs.state_id == self.id:
                    objs.append(obj)

            return objs
