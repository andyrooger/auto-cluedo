'''
Created on 30 Dec 2012

@author: andyrooger
'''

class InformationStore:
    '''Base class for storing information about things. (Vague I know...)'''
    
    def __init__(self):
        self.__everything = set()
        self.__by_type = {}
    
    def add(self, info):
        self.__everything.add(info)
        type_name = info.__class__.__name__
        if not type_name in self.__by_type:
            self.__by_type[type_name] = set()
        self.__by_type[type_name].add(info)
    
    def all(self):
        return set(self.__everything)
    
    def of_type(self, t):
        return set(self.__by_type.get(t.__class__.__name__, set()))
    
    def __len__(self):
        return len(self.__everything)
