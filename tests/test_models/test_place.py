#!/usr/bin/python3
"""
Tests for the Place model
"""
from tests.test_models.test_base_model import test_BaseModel
from models.place import Place


class test_Place(test_BaseModel):
    """
    Define extra tests for the ``Place`` class
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the class' test
        """
        super().__init__(*args, **kwargs)
        self.value = Place
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
        - city_id -> string
        - user_id -> string
        - name -> string
        - description -> string
        - number_rooms -> integer
        - number_bathrooms -> integer
        - max_guest -> integer
        - price_by_night -> integer
        - latitude -> float
        - longitude -> float
        - amenity_ids -> list of string
        """
        _cls = Place

        foo = _cls()
        attrs = {'city_id': str, 'user_id': str, 'name': str,
                 'description': str, 'number_rooms': int,
                 'number_bathrooms': int, 'max_guest': int,
                 'price_by_night': int, 'latitude': float, 'longitude': float,
                 'amenity_ids': list}

        for attr, attr_type in attrs.items():
            with self.subTest(attr=attr, attr_type=attr_type):
                self.assertTrue(hasattr(foo, attr))
                self.assertEqual(type(getattr(foo, attr)), attr_type)
