#!/usr/bin/python3
"""FileStorage engine module."""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to JSON and deserializes back."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary of stored objects."""
        return self.__objects

    def new(self, obj):
        """Add new object to storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to JSON file."""
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(
                {k: v.to_dict() for k, v in self.__objects.items()},
                file
            )

    def reload(self):
        """Deserialize JSON file to objects."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for obj in data.values():
                    cls = eval(obj["__class__"])
                    self.new(cls(**obj))
        except FileNotFoundError:
            pass
