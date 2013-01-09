'''
Created on 30 Dec 2012

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
        return iter(self.__everything)
    
    def of_type(self, t):
        return iter(self.__by_type.get(t.__class__.__name__, set()))
    
    def __len__(self):
        return len(self.__everything)
