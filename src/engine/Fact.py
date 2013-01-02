'''
Created on 28 Dec 2012

@author: andyrooger
'''
from engine.InformationStore import InformationStore
from engine.EqualsMixin import EqualsMixin

class Fact(EqualsMixin):
    '''
    Describes a fact, something we definitely know about the game
    that happened at a particular time.
    '''

    def __init__(self, factstore=None):
        self.factstore = factstore or _DEFAULT_FACT_STORE
        self.at = self.factstore.get_next_time()
        self.factstore.add(self)
    
    def _key(self):
        return (self.at, self.factstore)

class FactStore(InformationStore):
    '''Stores a collection of facts and allows retrieving them by type or all together.'''
    
    def __init__(self):
        super().__init__()
        self._current_time = 0
    
    def current_time(self):
        return self._current_time
    
    def get_next_time(self):
        self._current_time += 1
        return self._current_time
    
    def add(self, info):
        if not isinstance(info, Fact):
            raise TypeError("Can only add facts to fact store.")
        if info.factstore is not self:
            raise ValueError("Fact is not from this store.")
        InformationStore.add(self, info)

_DEFAULT_FACT_STORE = FactStore()