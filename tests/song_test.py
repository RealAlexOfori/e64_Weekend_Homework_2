import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Christlight", "Alex Ofori")
        # self.song_2 = Song("Jesus is Lord", "Kanye West")
        # self.song_3 = Song("Redemption Song", "Bob Marley")
        # self.song_4 = Song("Changes", "Tupac")
        # self.song_5 = Song("Get Busy", "Sean Paul")

        # self.songs = [self.song_1, self.song_2, self.song_3, self.song_4, self.song_5]

    def test_song_has_a_title(self):
        self.assertEqual("Christlight", self.song.title)

    def test_song_has_an_artist(self):
        self.assertEqual("Alex Ofori", self.song.artist)



