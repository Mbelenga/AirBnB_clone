#!/usr/bin/python3
"""
This is an init model
It is supposed to create a unique File Storage
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
