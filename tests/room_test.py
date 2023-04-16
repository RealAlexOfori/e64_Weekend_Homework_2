import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Christlight", "Alex Ofori")
        self.song_2 = Song("Jesus is Lord", "Kanye West")
        self.song_3 = Song("Be Still", "Hillsong")
        

        self.songs = [self.song_1, self.song_2, self.song_3]

        self.guest_1 = Guest("Alex", 30)
        self.guest_2 = Guest("Daniel", 17)
        self.guest_3 = Guest("John", 7)

        self.guests = [self.guest_1,self.guest_2,self.guest_3]

        self.room = Room("Gospel Room", 3, 15)


    def test_room_has_a_name(self):
        self.assertEqual("Gospel Room", self.room.name)

    def test_room_has_no_guest(self):
        self.assertEqual(0, self.room.number_of_guests())

    def test_room_has_no_songs(self):
        self.assertEqual(0,self.room.number_of_songs())

    def test_check_in_guest_to_room(self):
        self.room.add_guest(self.guests)
        self.assertEqual(1, self.room.number_of_guests())

    def test_add_song_to_room(self):
        self.room.add_song(self.songs)
        self.assertEqual(1, self.room.number_of_songs())

    def test_add_songs_to_room(self):
        self.room.add_songs(self.songs)
        self.assertEqual(3, self.room.number_of_songs())


    def test_check_in_guest_to_room(self):
        self.room.add_guests(self.guests)
        self.assertEqual(3, self.room.number_of_guests())

    def test_check_out_guest(self):
        self.room.add_guests(self.guests)
        self.room.check_out_guest(self.guest_1)
        self.assertEqual(2, self.room.number_of_guests())

    def test_cannot_add_guest_if_at_capacity(self):
        self.room.add_guests(self.guests)
        self.assertEqual("no more capacity",self.room.add_guest(self.guest_2) )

    def test_guest_cannot_afford(self):
        self.assertEqual("cannot afford", self.room.add_guest(self.guest_3))


    