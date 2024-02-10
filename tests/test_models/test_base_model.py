#!usr/bin/python3
"""
Testing the base model class
"""

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """The test case for the basemodel class"""

    def setUp(self):
        """It creates an instance of the basemodel class"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Deletes the base model object like cleaning it up"""
        del self, base_model

    def test_id(self):
        """This tests the id"""
        self.assertEqual(self.base_model.id, str)

    def test_created_at(self):
        "This tests the created at"""
        self.assertEqual(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """Tests the updated_at"""
        self.assertEqual(self.base_model.updated_at, datetime)

    def test_str(self):
        """Tests the __str__ method"""
        self.assertTrue(isinstance(self.base_model.__str__(), str))

    def test_save(self):
        initial_time = self.base_model.updated_at
        self.base_model.save()
        self.assertLess(initial_time, self.base_model.updated_at)

    def test_to_dict(self):
        """Checks the to_dict """
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIsInstance('id', model_dict)
        self.assertIsInstance('created_at', model_dict)
        self.assertIsInstance('updated_at', model_dict)
        self.assertTrue(model_dict['__class__'], 'BaseModel')


if '__name__' == '__main__':
    unittest.main()
