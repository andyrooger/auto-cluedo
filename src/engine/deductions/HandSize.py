'''
Created on 1 Jan 2013

@author: andyrooger
'''
from engine.Deduction import Deduction

class HandSize(Deduction):
    '''Describes knowledge of how many cards someone has at a particular time.'''
    
    def __init__(self, deductionstore, player, size, at, *relieson):
        super().__init__(deductionstore, *relieson)
        self.player = player
        self.size = size
        self.at = at
    
    def _key(self):
        return (super()._key(), self.player, self.size, self.at)
