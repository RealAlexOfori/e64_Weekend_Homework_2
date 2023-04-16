import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Alex", 30)

    def test_guest_has_a_name(self):
        self.assertEqual("Alex", self.guest.name)
                    
    
        

    