#!/usr/bin/python3
"""
It defines the user class
Inherits from the BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class helps us create a user

    Its Attributes:
        * Email: Has the email of the user
        * Password: Has the users password
        * First_name : Has the users first name
        * Last_name : Has the users last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
