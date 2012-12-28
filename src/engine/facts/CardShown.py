'''
Created on 29 Dec 2012

@author: andyrooger
'''
from engine.Fact import Fact

class CardShown(Fact):
    '''
    Describes an entry being shown to a player.
    '''
    
    def __init__(self, factstore, shower, showee, entry):
        super().__init__(factstore)
        self.shower = shower
        self.showee = showee
        self.entry = entry
    
    def _key(self):
        return (super()._key(), self.shower, self.showee, self.entry)
