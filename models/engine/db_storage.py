#!/usr/bin/python3
"""This module defines a class to manage database storage"""
import os
from models.base_model import Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """create engine and connect to database"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(user, pwd, db),
                                      pool_pre_ping=True)

        env = os.environ.get('HBNB_ENV')
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            result = self.__session.query(User, State, City,
                                          Amenity, Place, Review).all()
        else:
            result = self.__session.query(cls).all()
        obj_dict = {}

        for obj in result:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def delete(self, obj=None):
        """a public instance method to delete obj from"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage from database"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(autocommit=False,
                               autoflush=False,
                               bind=self.__engine,
                               expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """close method on class Session"""
        self.__session.close()
