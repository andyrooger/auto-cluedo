'''
Created on 30 Dec 2012

@author: andyrooger
'''

class NotHasCard(object):
    '''A user definitely does not have a card.'''
    
    def __init__(self, deductionstore, player, entry, at, *relieson):
        super().__init__(deductionstore, *relieson)
        self.player = player
        self.entry = entry
        self.at = at
    
    def _key(self):
        return (super()._key(), self.player, self.entry, self.at)
