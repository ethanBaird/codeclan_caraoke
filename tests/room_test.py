import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink



class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 5)
        self.guest = Guest("Ethan", 40, "Famous Last Words")
        self.song = Song("Famous Last Words", "My Chemical Romance")
        self.drink = Drink("Beer", 5)

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
        self.room.add_song(self.song, self.guest)
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

    def test_guest_cheers_for_fave_song_when_added(self):
        self.assertEqual("YALDI", self.room.add_song(self.song, self.guest))

    def test_guest_asks_for_fave_song_if_not_fave_added(self):
        self.not_fave_song = Song("One More Time", "Britney Spears")
        self.assertEqual("Can somebody queue Famous Last Words!", self.room.add_song(self.not_fave_song, self.guest))

    def test_room_can_sell_drink(self):
        self.room.sell_drink(self.guest, self.drink)

        self.assertEqual(5, self.room.till)
        self.assertEqual(35, self.guest.wallet)