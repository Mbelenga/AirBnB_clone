#!/usr/bin/python3
"""
This modules defines the Review class
It inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This represents a Review class
    Public class atttributes:
    place_id:string-empty  string
    user_id:string-empty string
    text:string -empty_string
    """
    place_id = ""
    user_id = ""
    text = ""
