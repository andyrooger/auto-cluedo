'''
Created on 1 Jan 2013

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

from engine.Rule import Rule
from engine.deductions.HandSize import HandSize

class InitialHandSize(Rule):
    '''Always applies and sets each player's hand to zero initially.'''

    def __init__(self, *players):
        super().__init__()
        self.players = players
    
    def apply(self, add, factstore, deductionstore):
        for player in self.players:
            add(HandSize, player, 0, 0)
        
