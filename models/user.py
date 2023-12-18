#!/usr/bin/python3
"""
class User which inherits from BaseModel
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    Represent a User
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
