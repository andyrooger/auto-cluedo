'''
Created on 2 Jan 2013

@author: andyrooger
'''

# auto-cluedo
# Copyright (C) 2013  Andy Gurden
# 
#     This file is part of auto-cluedo.
# 
#     auto-cluedo is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     auto-cluedo is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with auto-cluedo.  If not, see <http://www.gnu.org/licenses/>.

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
    
