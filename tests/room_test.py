import unittest

from classes.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 15)

    def test_room_has_number(self):
        self.assertEqual(1, self.room.room_number)

    # @unittest.skip("skip for now")
    def test_room_has_capacity(self):
        self.assertEqual(15, self.room.capacity)

    def test_room_starts_empty(self):
        self.assertEqual(0, self.room.get_guests())

    
