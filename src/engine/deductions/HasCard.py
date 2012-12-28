'''
Created on 30 Dec 2012

@author: andyrooger
'''
from engine.Deduction import Deduction

class HasCard(Deduction):
    '''Describes a user having a card at a particular time.'''
    
    def __init__(self, deductionstore, player, entry, at, *relieson):
        super().__init__(deductionstore, *relieson)
        self.player = player
        self.entry = entry
        self.at = at
    
    def _key(self):
        return (super()._key(), self.player, self.entry, self.at)
