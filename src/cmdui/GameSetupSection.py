'''
Created on 2 Jan 2013

@author: andyrooger
'''
from cmdui.base.CommandSection import CommandSection

class GameSetupSection(CommandSection):
    '''Setup stage of the game. Will return a dict containing the game setup.'''
    
    def __init__(self):
        super().__init__("You must first complete the game setup.")
    
    def start(self):
        super().start()
        return {"total_cards": 30, "player_order": ["ME", "SOMEONE ELSE", "AND ONE OTHER"]}
