#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ as env

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel, Base):
    """ State class / table model"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                            cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """get all cities with the current state id
        from filestorage
        """
        from models import storage
        if env.get('HBNB_TYPE_STORAGE') != 'db':
            return [
                v for k, v in storage.all(City).items()
                if v.state_id == self.id
            ]
        raise AttributeError()
