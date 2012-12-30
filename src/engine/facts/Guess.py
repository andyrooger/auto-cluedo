'''
Created on 28 Dec 2012

@author: andyrooger
'''
from engine.Fact import Fact

class Guess(Fact):
    '''
    Describes a guess by a player, asking a single other player.
    '''

    def __init__(self, factstore, asker, answerer, showed, *entries):
        super().__init__(factstore)
        self.asker = asker
        self.answerer = answerer
        self.showed = showed
        self.entries = entries
    
    def _key(self):
        return (super()._key(), self.asker, self.answerer, self.showed, self.entries)
