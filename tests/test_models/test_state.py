#!/usr/bin/python3
"""
Tests for the State model
"""
import models
import unittest
from tests.test_models.test_base_model import test_BaseModel
from models.state import State


class test_State(test_BaseModel):
    """
    Define extra tests for the ``State`` class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the class' test
        """
        super().__init__(*args, **kwargs)
        self.value = State
        self.name = self.value.__name__

    def setUp(self):
        """
        Set up for tests
        """
        super().setUp()

    def tearDown(self):
        """
        Tear down for the tests
        """
        super().tearDown()

    @unittest.skipUnless(models.storage_type == 'file', "Using file storage")
    def test_user_attrs(self):
        """
        Ensure that the correct attributes are present in the model
        Namely:
        - name -> string
        """
        _cls = State

        foo = _cls()
        attrs = {'name': str}

        for attr, attr_type in attrs.items():
            with self.subTest(attr=attr, attr_type=attr_type):
                self.assertTrue(hasattr(foo, attr))
                self.assertEqual(type(getattr(foo, attr)), attr_type)
