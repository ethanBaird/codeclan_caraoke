import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Ethan", 40)

    def test_guest_has_name(self):
        self.assertEqual("Ethan", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(40, self.guest.wallet)

    

