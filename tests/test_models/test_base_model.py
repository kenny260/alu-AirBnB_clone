#!/usr/bin/python3
"""Unittests for BaseModel class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel."""

    def test_instance_creation(self):
        """Test BaseModel instance creation."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_is_string(self):
        """Test that id is a string."""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_created_at_is_datetime(self):
        """Test created_at attribute."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test updated_at attribute."""
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str_method(self):
        """Test __str__ method output."""
        obj = BaseModel()
        expected = "[{}] ({}) {}".format(
            obj.__class__.__name__,
            obj.id,
            obj.__dict__
        )
        self.assertEqual(str(obj), expected)

    def test_save_updates_updated_at(self):
        """Test save method updates updated_at."""
        obj = BaseModel()
        old_time = obj.updated_at
        obj.save()
        self.assertNotEqual(old_time, obj.updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
