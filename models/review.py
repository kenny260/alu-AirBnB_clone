#!/usr/bin/python3
"""Review module - defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class - represents a review"""
    place_id = ""
    user_id = ""
    text = ""
