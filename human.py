from player import Player

class Human(Player):
    def __init__(self):
        self.name = input("Please type your name  ")

        super().__init__()

    def choose_gesture(self):
        print(f"{self.name}, here are your RPSLS gesture choices:")
        for gesture in self.gesture:
            print(gesture)
        print("\n")