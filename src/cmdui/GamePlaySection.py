'''
Created on 2 Jan 2013

@author: andyrooger
'''
from cmdui.base.CommandSection import CommandSection

class GamePlaySection(CommandSection):
    '''The looping turn based game play.'''

    def __init__(self, engine, total_cards, player_order):
        super().__init__("Time to play!")
        