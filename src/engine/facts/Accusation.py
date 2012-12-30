'''
Created on 29 Dec 2012

@author: andyrooger
'''
from engine.Fact import Fact

class Accusation(Fact):
    '''
    Describes an accusation.
    '''

    def __init__(self, factstore, player, correct, *entries):
        super().__init__(factstore)
        self.player = player
        self.correct = correct
        self.entries = set(entries)
    
    def _key(self):
        return (super()._key(), self.player, self.correct, self.entries)
