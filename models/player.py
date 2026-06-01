class Player:
    def __init__(self, player_number, name, is_human):
        self.player_number = player_number
        self.name = name
        self.is_human = is_human
        self.character = None
        self.racket = None

    @property
    def label(self):
        return f"P{self.player_number} - {self.name}"

    def assign_character(self, character):
        self.character = character

    def assign_racket(self, racket):
        self.racket = racket