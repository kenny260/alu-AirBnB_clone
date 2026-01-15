#!/usr/bin/python3
"""Unit tests for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_city_inherits_from_base_model(self):
        """Test that City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_has_state_id_attr(self):
        """Test that City has state_id attribute"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")

    def test_city_has_name_attr(self):
        """Test that City has name attribute"""
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")

    def test_city_attrs_are_strings(self):
        """Test that City attributes are strings"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)


if __name__ == '__main__':
    unittest.main()
