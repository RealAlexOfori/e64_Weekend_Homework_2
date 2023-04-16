class Room:
    def __init__(self, name, capacity, entryfee):
        self.name = name
        self.songs = []
        self.guests = []
        self.capacity = capacity
        self.entryfee = entryfee


    def number_of_guests(self):
        return len(self.guests)
    
    def number_of_songs(self):
        return len(self.songs)
    
    def add_guest(self,guest):
        return self.guests.append(guest)
    
    def add_song(self, song):
        return self.songs.append(song)
    
    def add_songs(self, songs):
        for song in songs:
           self.songs.append(song)

    def add_guests(self, guests):
        for guest in guests:
            self.guests.append(guest)

    def check_out_guest(self, guest):
        if guest in self.guests:
          self.guests.remove(guest)

    def add_guest(self, guest):
        if len(self.guests) >= self.capacity:
           return "no more capacity"
        if guest.wallet < self.entryfee:
            return "cannot afford"
        else:
            self.guests.append(guest)