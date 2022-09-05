import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o -- represents human or computer
        self.letter = letter

    def get_move(self, game):
        pass

class RandomCompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
        
