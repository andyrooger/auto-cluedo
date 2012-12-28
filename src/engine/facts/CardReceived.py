'''
Created on 28 Dec 2012

@author: andyrooger
'''
from engine.Fact import Fact

class CardReceived(Fact):
    '''
    Describes the point at which a card is picked up.
    '''

    def __init__(self, factstore, player):
        super().__init__(factstore)
        self.player = player
    
    def _key(self):
        return (super()._key(), self.player)
