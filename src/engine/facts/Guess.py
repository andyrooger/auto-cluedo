'''
Created on 28 Dec 2012

@author: andyrooger
'''
from engine.Fact import Fact

class Guess(Fact):
    '''
    Describes a guess by a player, asking a single other player.
    '''


    def __init__(self, asker, answerer, showed, *entries):
        super().__init__()
        self.asker = asker
        self.answerer = answerer
        self.showed = showed
        self.entries = entries