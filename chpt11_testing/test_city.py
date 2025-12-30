"""Test Module for city_country.py"""

import unittest
from city_country import city_country as cc

class CityTestCase(unittest.TestCase):
    """Test case for city_country.py"""
    
    def test_city_country(self):
        """Test if Lagos, Nigeria works!"""
        location = cc('lagos', 'nigeria')
        self.assertEqual(location, 'Lagos, Nigeria')
        
    def test_population(self):
        """Test if adding population parameter works: Lagos, Nigeria - 5000000"""
        location = cc('lagos', 'nigeria', 5000000)
        self.assertEqual(location, 'Lagos, Nigeria - Population 5000000')

unittest.main()

