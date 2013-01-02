'''
Created on 1 Jan 2013

@author: andyrooger
'''
from engine.Rule import Rule
from engine.deductions.HandSize import HandSize

class InitialHandSize(Rule):
    '''Always applies and sets each player's hand to zero initially.'''

    def __init__(self, *players):
        super().__init__()
        self.players = players
    
    def apply(self, add):
        for player in self.players:
            add(HandSize, player, 0, 0)
        