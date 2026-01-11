#!/usr/bin/python3
"""FileStorage module."""

import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes back."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add new object to storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects to JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                f
            )

    def reload(self):
        """Deserialize JSON file to objects."""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objs = json.load(f)
                for key, value in objs.items():
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
