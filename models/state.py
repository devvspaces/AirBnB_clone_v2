#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ as env

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel
from models.city import City
import env


class State(BaseModel, Base):
    """ State class / table model"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    __cities = relationship('City', backref='state',
                            cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """get all cities with the current state id
        from filestorage
        """
        if env.HBNB_TYPE_STORAGE != 'db':
            from models import storage
            return [
                v for k, v in storage.all(City).items()
                if v.state_id == self.id
            ]
        return self.__cities
