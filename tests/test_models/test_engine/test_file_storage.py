#!/usr/bin/python3
"""Unit tests for FileStorage class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Test that new adds an object to __objects"""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, storage.all())

    def test_save(self):
        """Test that save creates a file"""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test that reload loads objects from file"""
        storage = FileStorage()
        model = BaseModel()
        model.name = "Test"
        storage.new(model)
        storage.save()
        storage2 = FileStorage()
        storage2.reload()
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, storage2.all())


if __name__ == '__main__':
    unittest.main()
