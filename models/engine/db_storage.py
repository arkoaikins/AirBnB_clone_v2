#!/usr/python3
"""
Module for Database Storage
"""
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import (sessionmaker, scoped_session)


class DBStorage:
    """
    Definition of DBStorage class
    """
    __engine = None
    __session = None
    __env = None    # Environmental variables

    def __init__(self):
        """
        Initialization
        """
        env_vars = {
                'user': "HBNB_MYSQL_USER",
                'pwd': "HBNB_MYSQL_PWD",
                'host': "HBNB_MYSQL_HOST",
                'db': "HBNB_MYSQL_DB",
                'env': "HBNB_ENV"}

        self.__env = dict()

        for var in env_vars.values():
            value = getenv(var)

            if value is None and var != env_vars['env']:
                print("** environmental variable '{}' is {} \
**".format(var, value))
                print("** Impossible to user {} \
**".format(self.__class__.__name))
                exit(1)
            else:
                self.__env.update({var: value})

        # Add port
        env_vars.update({'port': "HBNB_MYSQL_PORT"})
        self.__env.update({env_vars['port']: 3306})

        # Create engine
        conn_url = "mysql+mysqldb://{}:{}@{}:{}/{}".format(
                self.__env[env_vars['user']],
                self.__env[env_vars['pwd']],
                self.__env[env_vars['host']],
                self.__env[env_vars['port']],
                self.__env[env_vars['db']])

        self.__engine = create_engine(conn_url, pool_pre_ping=True, echo=False)

        # If in test environment
        if self.__env[env_vars['env']] == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Return all objeccts based on or not on the class
        if cls is invalid, an empty dictionary is returned
        """
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity

        # Update it Always after mapping a class
        # classes = [City, State, Place, User, Amenity, Review]
        classes = [City, State, User, Place, Review, Amenity]

        objs = list()
        if cls is None:
            for a_class in classes:
                objs += self.__session.query(a_class)\
                        .order_by(a_class.id)\
                        .all()
        elif cls in classes:
            objs = self.__session.query(cls)\
                    .order_by(cls.id)\
                    .all()
        else:
            return dict()

        # Modify objects so that the result will be a dictionary of
        # key, value pairs where
        # key = <class name>.<object id>
        # value = object
        objs_dict = dict()
        for value in objs:
            key = type(value).__name__ + '.' + value.id
            objs_dict.update({key: value})

        return objs_dict

    def new(self, obj):
        """
        Add the object to the current database session
        """
        if obj is not None:
            self.__session.add(obj)
            self.save()

    def save(self):
        """
        Save changes made by this current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete object from session
        """
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
        SESSION CONFIGURATION
        =====================
        Create all tables if not existing and create a database session
        """
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity

        # Create all tables
        Base.metadata.create_all(self.__engine)

        # Create current database session
        # The option expire_on commit must be False
        # and scoped_session is used to ensure the Session is thread-safe
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)  # global scope

        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Close connection to database storage
        """
        self.__session.close()
