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
        (factstore or __DEFAULT_FACT_STORE).add_fact(self)

class FactStore:
    '''Stores a collection of facts and allows retrieving them by type or all together.'''
    
    def __init__(self):
        self.__facts = []
        self.__by_type = {}
    
    def add_fact(self, fact):
        self.__facts.append(fact)
        type_name = fact.__class__.__name__
        if not type_name in self.__by_type:
            self.__by_type[type_name] = []
        self.__by_type[type_name].append(fact)

__DEFAULT_FACT_STORE = FactStore()