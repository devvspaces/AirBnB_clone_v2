#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import env
from sqlalchemy import text


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), type(None))

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), type(None))

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), type(None))

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), type(None))


# class test_User_db(unittest.TestCase):
#     """
#     Test the User class with DBStorage
#     """

#     def __init__(self, *args, **kwargs):
#         """ """
#         super().__init__(*args, **kwargs)
#         self.name = "User"
#         self.value = User

#     def test_save(self):
#         """
#         Test save method
#         """
#         from models import storage
#         session = storage.session
        
