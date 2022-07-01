import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song



class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 5)
        self.guest = Guest("Ethan", 40, "Famous Last Words")
        self.song = Song("Famous Last Words", "My Chemical Romance")

    def test_room_has_number(self):
        self.assertEqual(1, self.room.room_number)

    # @unittest.skip("skip for now")
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)

    def test_room_starts_empty(self):
        self.assertEqual(0, self.room.get_guests())

    def test_room_can_check_in_guest(self):
        self.room.check_in(self.guest)
        self.assertEqual(1, self.room.get_guests())

    def test_room_can_check_out_guest(self):
        self.room.check_in(self.guest)
        self.room.check_out(self.guest)

        self.assertEqual(0, self.room.get_guests())

    def test_room_can_add_song(self):
        self.room.add_song(self.song)
        self.assertEqual(1, self.room.get_songs())

    def test_room_can_not_exceed_capacity(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        self.room.check_in(self.guest)
        
        self.assertEqual("Room Full", self.room.check_in(self.guest))
        self.assertEqual(5, self.room.get_guests())

    def test_room_charges_guest_on_check_in(self):
        self.room.check_in(self.guest)

        self.assertEqual(10, self.room.till)
        self.assertEqual(30, self.guest.wallet)

