#!/usr/bin/python3
"""Unit tests for User class"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_user_inherits_from_base_model(self):
        """Test that User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_has_email_attr(self):
        """Test that User has email attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, "")

    def test_user_has_password_attr(self):
        """Test that User has password attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'password'))
        self.assertEqual(user.password, "")

    def test_user_has_first_name_attr(self):
        """Test that User has first_name attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, "")

    def test_user_has_last_name_attr(self):
        """Test that User has last_name attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.last_name, "")

    def test_user_attr_are_strings(self):
        """Test that User attributes are strings"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)


if __name__ == '__main__':
    unittest.main()
