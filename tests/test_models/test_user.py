#!/usr/bin/python3
"""Unittests for the User class."""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class."""

    def test_user_is_instance(self):
        """Test that User is an instance of BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes_exist(self):
        """Test that User has expected attributes."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))


if __name__ == "__main__":
    unittest.main()
