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

    def sufficient_funds(self, drink):
        return self.wallet >= drink.price

    def buy_drink(self, drink):
        if self.sufficient_funds(drink):
            self.wallet -= drink.price
        else:
            pass




    