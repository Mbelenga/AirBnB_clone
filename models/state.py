#!/user/bin/python3
"""
Defines the state class
Inherits from the basemodel
"""

from models.base_model import Base_model


class State(BaseModel):
    """
    Inherits from the baseclass
    name(str): This is a string which represents the name of the state
    """
    name = ""
