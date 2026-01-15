#!/usr/bin/python3
"""City module - defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class - represents a city"""
    state_id = ""
    name = ""
