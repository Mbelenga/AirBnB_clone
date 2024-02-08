#!/usr/bin/python3
""""
Defines the basemodel class which provides the public instance
attributes and methods and also the serialization/deserialization
process.
""""
import uuid
from datetime import datetime
import models

class BaseModel:
""""
A BaseModel class
""""
def __init__(self, *args, *kwargs):
    """"
    Initializing an instance of the base model class the attributes
    to be used created_at and updated_at which are datetime attribute
    the id which is a string attrbute.
    The methods to be used include __str__method tha t returns a string
    representation of the object.
    """"
if kwargs:
    for key, value in kwargs.items():
        if key == "created_at" or key == "updated_at":
            value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        setattr(self, key, value)
    else:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.upated_at = self.created_at
        models.storage.new(self)