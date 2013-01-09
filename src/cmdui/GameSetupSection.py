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
from engine.Engine import Engine
from engine.rules.InitialHandSize import InitialHandSize
from engine.facts.CardReceived import CardReceived
from timeit import itertools

class GameSetupSection(CommandSection):
    '''Setup stage of the game. Will return a tuple of engine, total_cards, player_order.'''
    
    def __init__(self):
        super().__init__("You must first complete the game setup.")
    
    def start(self):
        super().start()
        total_cards = self.get_total_cards()
        player_order = self.get_player_order()
        engine = Engine([InitialHandSize(player_order)])
        self.deal_cards(engine, total_cards, player_order)
        return (engine, total_cards, player_order)
    
    def get_total_cards(self):
        return 30 # TODO
    
    def get_player_order(self):
        return ["ME", "SOMEONE ELSE", "AND ONE OTHER"] # TODO
    
    def deal_cards(self, engine, cards, player_order):
        cards_left = cards
        for player in itertools.cycle(player_order):
            if cards_left:
                engine.add_fact(CardReceived, player)
                cards_left -= 1
            else:
                break
