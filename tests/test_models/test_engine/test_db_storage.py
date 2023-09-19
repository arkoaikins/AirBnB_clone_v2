#!/usr/bin/python3
"""
Tests for the Database storage

Execution:
     HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd
     HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db
     HBNB_TYPE_STORAGE=db python3 -m unittest discover tests
"""
import unittest
import pep8
import MySQLdb
import models
from models import storage_type
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from tests import config
from os import getenv
from utility import execsafe
from unittest import (skipIf, skipUnless)


class test_DBStorage(unittest.TestCase):
    """
    Define tests for the ``DBStorage`` class
    """
    # Set maxDiff to see all output on error comparison
    maxDiff = None

    def __init__(self, *args, **kwargs):
        """
        Initialiaze the test instance
        """
        super().__init__(*args, **kwargs)
        if storage_type == 'file':
            print("Iniatialization for database")
            return
        self.value = DBStorage
        self.name = self.value.__name__

        self.db_login = {
                'host':     getenv('HBNB_MYSQL_HOST'),
                'user':     getenv('HBNB_MYSQL_USER'),
                'passwd':   getenv('HBNB_MYSQL_PWD'),
                'db':       getenv('HBNB_MYSQL_DB'),
                'port':     getenv('HBNB_MYSQL_PORT')}

        # Defaults
        if self.db_login['port'] is None:
            self.db_login['port'] = 3306
        if self.db_login['host'] is None:
            self.db_login['host'] = 'localhost'

        # Connection to database
        for key, val in self.db_login.items():
            if val is None:
                print("key: {} => value : {}".format(key, val))     # test
                return  # not necessary to proceed

        # Create a connection
        self.db = MySQLdb.connect(**self.db_login)
        # Put a connection to a good use
        self.cur = self.db.cursor()
        print("cursor created successfully!\n")     # test

    '''
    def setUp(self):
        """
        Set up the environment for each test methods
        Clean all tables in the database
        """
        # Clean up the database
        query = """SHOW TABLES;"""
        params = self.db_login['db']

        # Execute query
        if execsafe(self.cur, query) is False:
            print("Could not execute query")
            return

        print("Successfully executed query")
        tbs = self.cur.fetchall()
        print("Tables present")
        print(tbs)

        ordered_tbs = ['users', 'states', 'cities', 'places', 'amenities']
        for tb in ordered_tbs:
            if (tb,) not in tbs:
                continue
            query = """TRUNCATE TABLE {0};""".format(tb)
            if not execsafe(self.cur, query):
                print("Could not fetch table -> {}".format(tb[0]))
                return

            print("Succesfully fetched table -> {}".format(tb[0]))
            recs = self.cur.fetchall()
            if recs is not None:
                for row in recs:
                    print(row)
    '''

    def setUp(self):
        """
        Set up the environment for each test methods
        Get current state of database
        """
        print("storage_type is {}".format(storage_type))    # test
        if storage_type == 'file':
            return

        execsafe(self.cur, """SELECT * FROM states;""")
        self.states = self.cur.fetchall()

        execsafe(self.cur, """SELECT * FROM places;""")
        self.places = self.cur.fetchall()

        execsafe(self.cur, """SELECT * FROM amenities;""")
        self.amenities = self.cur.fetchall()

        execsafe(self.cur, """SELECT * FROM reviews;""")
        self.reviews = self.cur.fetchall()

        execsafe(self.cur, """SELECT * FROM users;""")
        self.users = self.cur.fetchall()

        execsafe(self.cur, """SELECT * FROM cities;""")
        self.cities = self.cur.fetchall()

        print("Set up for database done successfully\n")    # test

    def tearDown(self):
        """
        Finishing tasks for a test
        """
        if storage_type == 'file':
            return
        self.db.commit()
        print("Tear down for database done successfully\n")     # test

    @skipIf(storage_type == 'file', "This test is for datbase storage")
    def test_all(self):
        """
        Testing the all method
        """
        state_1 = State(name="Ezra")
        state_1 = state_1.to_dict()
        query = """INSERT INTO states(id, name, updated_at, created_at)
                    VALUES ('{}', '{}', '{}', '{}')""".format(
                    state_1['id'], state_1['name'], state_1['updated_at'],
                    state_1['created_at'])
        execsafe(self.cur, query)
        # self.db.commit()
        execsafe(self.cur, """SELECT * FROM states;""")
        states = self.cur.fetchall()
        print("len(self.states): {}".format(len(self.states)))
        print("len(states): {}".format(len(states)))
        self.assertTrue(len(states) == len(self.states) + 1)
