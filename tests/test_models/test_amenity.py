#!/usr/bin/python3
"""This is a file that cointains the unittest for the amenity class"""

import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """This is a unittest for testing the Amenity class"""
    def setUp(self):
        """This is an instance of an amenity"""
        self.my_amenity = Amenity()

    def tearDown(self):
        """It cleans up the amenity instance"""
        del self.my_amenity


if __name__ == "__main__":
    unittest.main()
