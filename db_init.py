#!/usr/bin/python3
"""
This module sets some instance in the database for a fresh start

Execution:
    HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd
    HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db
    HBNB_TYPE_STORAGE=db HBNB_ENB=test ./prog_name.py
"""
import models
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity


state_1 = State()
state_1.name = 'California'
state_1.save()
print("Created state_1 -> {}".format(state_1))

city_1 = City()
city_1.state_id = state_1.id
city_1.name = "San Francisco"
city_1.save()
print("Created city_1 -> {}".format(city_1))

city_2 = City()
city_2.state_id = state_1.id
city_2.name = "San Jose"
city_2.save()
print("Created city_2 -> {}".format(city_2))

user_1 = User()
user_1.email = 'onwutaebubegideon@gmail.com'
user_1.first_name = 'Ebube'
user_1.last_name = 'Onwuta'
user_1.password = 'ebube133pwd'
user_1.save()
print("Created user_1 -> {}".format(user_1))

user_2 = User()
user_2.email = "bob@hbtn.io"
user_2.password = 'bobpwd'
user_2.first_name = "Bob"
user_2.last_name = "Dylan"
user_2.save()
print("Created user_2 -> {}".format(user_2))

place_1 = Place()
place_1.city_id = city_1.id
place_1.user_id = user_1.id
place_1.name = 'Lovely place'
place_1.number_rooms = 3
place_1.number_bathrooms = 1
place_1.max_guest = 6
place_1.price_by_night = 120
place_1.latitude = 37.773972
place_1.longitude = 122.431297
place_1.save()
print("Created city_1 -> {}".format(place_1))

storage.save()
