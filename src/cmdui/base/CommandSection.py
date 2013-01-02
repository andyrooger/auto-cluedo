'''
Created on 2 Jan 2013

@author: andyrooger
'''

class CommandSection:
    '''A section of the command line UI. Performs a specific role.'''
    
    def __init__(self, intro=None):
        self._intro = intro
    
    def intro(self):
        return self._intro
    
    def start(self):
        '''Start the section and possibly return something useful.'''
        intro = self.intro()
        if intro is not None:
            print(intro)
    