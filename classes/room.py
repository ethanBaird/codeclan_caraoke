class Room:

    def __init__(self, _room_number, _capacity):
        self.room_number = _room_number
        self.capacity = _capacity
        self.till = 0
        self.guests = []
        self.songs = []

    def get_guests(self):
        return len(self.guests)

    def check_in(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
            self.till += 10
            guest.wallet -= 10
        else:
            return "Room Full"

    def check_out(self, guest):
        self.guests.remove(guest)

    def get_songs(self):
        return len(self.songs)

    def add_song(self, new_song, guest):
        repeat = False
        for song in self.songs:
            if song.title == new_song.title:
                repeat = True
        if repeat == False:
            self.songs.append(new_song)
            return guest.check_song(new_song)
        if repeat == True:
            pass

    def sell_drink(self, guest, drink):
        guest.buy_drink(drink)
        self.till += drink.price



