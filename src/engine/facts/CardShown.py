'''
Created on 29 Dec 2012

@author: andyrooger
'''
from engine.Fact import Fact

class CardShown(Fact):
    '''
    Describes an entry being shown to a player.
    '''
    
    def __init__(self, shower, showee, entry):
        super().__init__()
        self.shower = shower
        self.showee = showee
        self.entry = entry