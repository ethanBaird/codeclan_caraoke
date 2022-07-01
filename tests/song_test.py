import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Famous Last Words", "My Chemical Romance")

    def test_song_has_title(self):
        self.assertEqual("Famous Last Words", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("My Chemical Romance", self.song.artist)