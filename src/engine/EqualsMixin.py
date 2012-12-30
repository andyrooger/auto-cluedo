'''
Created on 30 Dec 2012

@author: andyrooger
'''

class EqualsMixin(object):
    '''Implements __eq__, __ne__, __hash__ based on _key(). By default this returns __dict__.'''
    
    def _key(self):
        return self.__dict__
    
    def __eq__(self, other):
        return other is not None and self._key() == other._key()
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self._key())
        