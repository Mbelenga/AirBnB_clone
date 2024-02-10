#!/usr/bin/python3
"""
This is a file storage class
serializes and desirializes the JSON file
"""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """
    This is a class that serializes and desirializes the JSON file
    """

    _file_path = "file.json"
    _objects = {}

    def all(self):
        """
        Returns a dictionary containing
        all objects
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary
        """
        class_name = obj.__class__.__name__
        self.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """
        serializes to a JSON file
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__filepath, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserialization of the json file
        """
        my_classes = {
                "BaseModel": BaseModel,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review,
                "User": User,
                }

        try:
            with open(self.__filepath, 'r') as file:
                my_dict = json.load(file)
                for key, value in my_dict.items():
                    class_name, my_id = key.split(".")
                    self.__objects[key] = self.my_class()[class_name](**value)
        except FileNotFoundError pass


storage = FileStorage()
storage.reload()
