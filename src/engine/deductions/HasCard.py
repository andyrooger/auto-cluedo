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

from engine.Deduction import Deduction

class HasCard(Deduction):
    '''Describes a user having a card at a particular time.'''
    
    def __init__(self, deductionstore, player, entry, at, *relieson):
        super().__init__(deductionstore, *relieson)
        self.player = player
        self.entry = entry
        self.at = at
    
    def _key(self):
        return (super()._key(), self.player, self.entry, self.at)
