# This class will define the player and what they can do

class Player:
    def __init__(self):
        self.actions = ["attack?", "role dice?", "explore?"]

    def choose_action(self):
        i = 1
        print("ACTIONS")
        for item in self.actions:
            print(str(i)+".", item)
            i += 1
