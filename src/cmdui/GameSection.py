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

from cmdui.base.CommandSection import CommandSection
from cmdui.GameSetupSection import GameSetupSection
from cmdui.GamePlaySection import GamePlaySection

class GameSection(CommandSection):
    '''Lets the user play through a game.'''
    
    def __init__(self):
        super().__init__("You have created a started a game.\n")
    
    def start(self):
        super().start()
        engine, total_cards, player_order = GameSetupSection().start()
        GamePlaySection(engine, total_cards, player_order).start()
