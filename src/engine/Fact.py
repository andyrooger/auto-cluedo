'''
Created on 28 Dec 2012

@author: andyrooger
'''

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
        self.factstore = (factstore or __DEFAULT_FACT_STORE)
        self.factstore.add_fact(self)
    
    def _key(self):
        return (self.at, self.factstore)
    
    def __eq__(self, other):
        return other is not None and self._key() == other._key()
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self._key())

class FactStore:
    '''Stores a collection of facts and allows retrieving them by type or all together.'''
    
    def __init__(self):
        self.__facts = set()
        self.__by_type = {}
    
    def add_fact(self, fact):
        self.__facts.add(fact)
        type_name = fact.__class__.__name__
        if not type_name in self.__by_type:
            self.__by_type[type_name] = set()
        self.__by_type[type_name].add(fact)

__DEFAULT_FACT_STORE = FactStore()