'''
Created on 2 Jan 2013

@author: andyrooger
'''
from cmdui.base.MenuSection import MenuSection

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
        print("Start game")
        return None
