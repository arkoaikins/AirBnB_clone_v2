#!/usr/bin/python3
"""
Tests for the City model
"""
from tests.test_models.test_base_model import test_BaseModel
from models.city import City


class test_City(test_BaseModel):
    """
    Define extra tests for the ``City`` class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the class' test
        """
        super().__init__(*args, **kwargs)
        self.value = City
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

    def test_user_attrs(self):
        """
        Ensure that the correct attributes are present in the model
        Namely:
        - state_id -> string
        - name -> string
        """
        _cls = City

        foo = _cls()
        attrs = {'state_id': str, 'name': str}

        for attr, attr_type in attrs.items():
            with self.subTest(attr=attr, attr_type=attr_type):
                self.assertTrue(hasattr(foo, attr))
                self.assertEqual(type(getattr(foo, attr)), attr_type)
