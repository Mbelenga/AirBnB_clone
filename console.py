#!/usr/bin/python3
"""
The Airbnb Console
The entry point of the command interpreter
"""
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from shlex import shlex
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    The HBNB class provides a command line interface
    """
    prompt = "(hbnb)"
    classes = {"BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review,
                }

    def emptyline(self):
        """Just an empty line"""
        pass

    def do_quit(self, cmd):
        """Handles the quit command"""
        return True

    def do_EOF(self, cmd):
        """Exits the program with(CTRL+D)"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
