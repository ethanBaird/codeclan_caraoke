class Guest:

    def __init__(self, _name, _wallet, _fave_song):
        self.name = _name
        self.wallet = _wallet
        self.fave_song = _fave_song

    def check_song(self, song):
        if self.fave_song == song.title:
            return "YALDI"
        else:
            return f"Can somebody queue {self.fave_song}!"

    def buy_drink(self, drink):
        self.wallet -= drink.price
        



    