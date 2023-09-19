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


class test_DBStorage(unittest.TestCase):
    """
    Define tests for the ``DBStorage`` class
    """
    # Set maxDiff to see all output on error comparison
    maxDiff = None

    @unittest.skipIf(storage_type == 'file', "For database storage")
    def __init__(self, *args, **kwargs):
        """
        Initialize the test instance
        """
        super().__init__(*args, **kwargs)
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

        # Connection to database
        db = MySQLdb.connect(**self.db_login)

        # Put a connection to a good use
        self.cur = db.cursor()

    @unittest.skipIf(storage_type == 'db', "For FileStorage")
    def __init__(self, *args, **kwargs):
        """
        Initialize the test instance
        """
        super().__init__(*args, **kwargs)
        pass

    @unittest.skipUnless(storage_type == 'db', 'For database storage')
    def setUp(self):
        """
        Set up the environment for each test method
        """
        # Clean up database
        query = """DROP DATABASE IF EXISTS %s"""
        params = self.db_login['db']

        """
        STOPPED HERE

        DROP ALL TABLES IN A DATABASE
        """
        # Execute query
        if execsafe(self.cur, query, (params,)) is False:
            print("Could not execute query")
        else:
            print("Successfully executed query")

    @unittest.skipIf(storage_type == 'db', 'For database storage')
    def tearDown(self):
        """
        Tear down the environment after each test method
        """
        # Clean up database
        query = """DROP DATABASE IF EXISTS %s;"""
        params = self.db_login['db']

        # Execute query
        execsafe(self.cur, query, (params,))

    def test_check_pep8_compliance(self):
        """
        Ensure all '*.py' files are pep8 (or pycodestyle) compliant
        It is ran only ``once`` during a test
        """
        if config.pep8_checked is False:
            path = "./"
            style = pep8.StyleGuide(quite=False, show_source=True,
                                    verbose=config.pep8_verbose)
            result = style.check_files(paths=path)
            self.assertEqual(result.total_errors, 0, "Fix pep8")
            config.pep8_checked = True

    '''
    @unittest.skipIf(models.storage_type == 'file', "For File storage system")
    def test_all(self):
        """
        Ensure that the `all` method is implemented
        Returns the dictionary of objects
        """
        storage = DBStorage()

        _cls = State()
        self.assertTrue(hasattr(storage, 'all'))
        self.assertEqual(type(storage.all()), dict)
    '''
