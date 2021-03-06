'''
Created on 28 Dec 2012

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

from engine.Fact import Fact

class Guess(Fact):
    '''
    Describes a guess by a player, asking a single other player.
    '''

    def __init__(self, factstore, asker, answerer, showed, *entries):
        super().__init__(factstore)
        self.asker = asker
        self.answerer = answerer
        self.showed = showed
        self.entries = set(entries)
    
    def _key(self):
        return (super()._key(), self.asker, self.answerer, self.showed, self.entries)
