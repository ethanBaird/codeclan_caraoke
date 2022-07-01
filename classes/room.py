class Room:

    def __init__(self, _room_number, _capacity):
        self.room_number = _room_number
        self.capacity = _capacity
        self.guests = []
        self.songs = {}

    def get_guests(self):
        return len(self.guests)

    def check_in(self, guest):
        self.guests.append(guest)

    def check_out(self, guest):
        self.guests.remove(guest)


