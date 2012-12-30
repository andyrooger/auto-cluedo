'''
Created on 28 Dec 2012

@author: andyrooger
'''
from engine.InformationStore import InformationStore

__last_time = 0

def get_next_time():
    __last_time += 1
    return __last_time

class Fact:
    '''
    Describes a fact, something we definitely know about the game
    that happened at a particular time.
    '''

    def __init__(self, factstore=None):
        self.at = get_next_time()
        self.factstore = (factstore or _DEFAULT_FACT_STORE)
        self.factstore.add(self)
    
    def _key(self):
        return (self.at, self.factstore)
    
    def __eq__(self, other):
        return other is not None and self._key() == other._key()
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self._key())

class FactStore(InformationStore):
    '''Stores a collection of facts and allows retrieving them by type or all together.'''
    
    def add(self, info):
        if not isinstance(info, Fact):
            raise TypeError("Can only add facts to fact store.")
        if info.factstore is not self:
            raise ValueError("Fact is not from this store.")
        InformationStore.add(self, info)

_DEFAULT_FACT_STORE = FactStore()