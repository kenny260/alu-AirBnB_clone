#!/usr/bin/python3
"""BaseModel module.

Defines the BaseModel class that serves as the base for all other models.
"""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel defines common attributes and methods for all models."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        If kwargs are provided, they are used to recreate the instance.
        Otherwise, a new instance is created with a unique id and timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Update the updated_at timestamp."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance.

        Includes the class name and converts datetime attributes to ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
