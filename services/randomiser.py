import random


class Randomiser:
    def assign(self, players, characters, rackets):
        if len(characters) < len(players):
            raise ValueError("Not enough characters available.")

        if len(rackets) < len(players):
            raise ValueError("Not enough rackets available.")

        chosen_characters = random.sample(characters, len(players))
        chosen_rackets = random.sample(rackets, len(players))

        for i, player in enumerate(players):
            player.assign_character(chosen_characters[i])
            player.assign_racket(chosen_rackets[i])