#!/usr/bin/python3
"""User module - defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class - represents a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
