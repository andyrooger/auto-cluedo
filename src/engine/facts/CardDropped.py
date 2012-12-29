'''
Created on 28 Dec 2012

@author: andyrooger
'''
from engine.Fact import Fact

class CardDropped(Fact):
    '''
    Describes the point at which a card is removed from a player's hand.
    '''


    def __init__(self, player):
        super().__init__()
        self.player = player