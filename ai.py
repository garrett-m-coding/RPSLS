from player import Player
import random

class Artificial(Player):
    def __init__(self):
        self.name = 'Smart-ass'
        super().__init__()

    def choose_gesture(self):
        return random.choice(self.gesture)