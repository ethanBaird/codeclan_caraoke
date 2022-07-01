import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Ethan", 40, "Famous Last Words")
        self.room = Room(23, 15)
        self.song = Song("Famous Last Words", "My Chemical Romance")


    def test_guest_has_name(self):
        self.assertEqual("Ethan", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(40, self.guest.wallet)

    def test_guest_has_fave_song(self):
        self.assertEqual("Famous Last Words", self.guest.fave_song)

    def test_guest_cheers_for_fave_song(self):
        self.room.add_song(self.song, self.guest)
        self.assertEqual("YALDI", self.guest.check_song(self.song))

    

    

