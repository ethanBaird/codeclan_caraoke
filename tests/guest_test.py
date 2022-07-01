import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.drink import Drink

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Ethan", 40, "Famous Last Words")
        self.room = Room(23, 15)
        self.song = Song("Famous Last Words", "My Chemical Romance")
        self.drink = Drink("Beer", 5)


    def test_guest_has_name(self):
        self.assertEqual("Ethan", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(40, self.guest.wallet)

    def test_guest_has_fave_song(self):
        self.assertEqual("Famous Last Words", self.guest.fave_song)

    def test_guest_cheers_for_fave_song(self):
        self.room.add_song(self.song, self.guest)
        self.assertEqual("YALDI", self.guest.check_song(self.song))

    def test_guest_can_buy_drink(self):
        self.guest.buy_drink(self.drink)

        self.assertEqual(35, self.guest.wallet)

    def test_guest_has_sufficient_funds(self):
        self.assertEqual(True, self.guest.sufficient_funds(self.drink))

    def test_guest_has_insufficient_funds(self):
        self.expensive_drink = Drink("Champagne", 50)
        self.assertEqual(False, self.guest.sufficient_funds(self.expensive_drink))

    def test_guest_can_buy_drink_with_sufficient_funds(self):
        self.guest.buy_drink(self.drink)
        self.assertEqual(35, self.guest.wallet)

    def test_guest_cant_buy_drink_with_insufficient_funds(self):
        self.expensive_drink = Drink("Champagne", 50)
        self.assertEqual(40, self.guest.wallet)

    

    

