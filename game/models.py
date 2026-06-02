from random import randint as rnd

class General_Player:
    def roll(self):
        return rnd(1, 6)


class Player(General_Player):
    def __init__(self, name):
        self.name = name
        self._score = 0
    
    def increase_score(self, new_score):
        self._score += new_score


class Computer(General_Player):
    def __str__(self):
        return f"I am your opponent for this game."
