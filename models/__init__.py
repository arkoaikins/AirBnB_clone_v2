#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


storage_type = os.getenv('HBNB_TYPE_STORAGE')
db_storage = 'db'
file_storage = 'file'

# Still using FileStorage -> Remove it after
# storage_type = 'file'

if storage_type == db_storage:
    storage = DBStorage()
if storage_type == file_storage:
    storage = FileStorage()

storage.reload()
