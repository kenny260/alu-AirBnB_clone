#!/usr/bin/python3
"""Unit tests for BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_init(self):
        """Test initialization"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_id_is_string(self):
        """Test that id is a string"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at_is_datetime(self):
        """Test that created_at is datetime"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is datetime"""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_unique_ids(self):
        """Test that two instances have different ids"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_str(self):
        """Test string representation"""
        model = BaseModel()
        string = str(model)
        self.assertIn('[BaseModel]', string)
        self.assertIn(model.id, string)

    def test_save(self):
        """Test save method"""
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(0.1)
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict contains correct keys"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_init_from_dict(self):
        """Test initialization from dictionary"""
        model = BaseModel()
        model.name = "Test"
        model.number = 123
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)
        self.assertEqual(model.name, new_model.name)
        self.assertEqual(model.number, new_model.number)

    def test_init_from_dict_datetime(self):
        """Test that datetime is correctly converted"""
        model = BaseModel()
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
