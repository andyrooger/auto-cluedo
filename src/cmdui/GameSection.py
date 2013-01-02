'''
Created on 2 Jan 2013

@author: andyrooger
'''
from cmdui.base.CommandSection import CommandSection
from cmdui.GameSetupSection import GameSetupSection
from engine.Engine import Engine
from engine.rules.InitialHandSize import InitialHandSize
from cmdui.GamePlaySection import GamePlaySection

class GameSection(CommandSection):
    '''Lets the user play through a game.'''
    
    def __init__(self):
        super().__init__("You have created a started a game.\n")
    
    def start(self):
        super().start()
        setup = GameSetupSection().start()
        engine = Engine([InitialHandSize(setup["player_order"])])
        GamePlaySection(engine, **setup).start()
        
        