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

from cmdui.base.MenuSection import MenuSection
from cmdui.GameSection import GameSection

class CommandUI:
    '''Main class for the command line UI for this program.'''
    
    def start(self):
        '''Begin input loop.'''
        MainMenu().start()

class MainMenu(MenuSection):
    def __init__(self):
        super().__init__("You have no game running, what would you like to do?",
                         [
                          ("Start a new game", "begin_game")
                          ], "Quit")
    
    def begin_game(self):
        GameSection().start()
        return None
