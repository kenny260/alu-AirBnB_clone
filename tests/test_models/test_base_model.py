#!/usr/bin/python3
"""Tests for BaseModel."""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel functionality."""

    def test_instance_creation(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_to_dict(self):
        obj = BaseModel()
        self.assertIn("__class__", obj.to_dict())


if __name__ == "__main__":
    unittest.main()
