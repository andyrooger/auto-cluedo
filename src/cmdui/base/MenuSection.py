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

class MenuSection(CommandSection):
    '''Represents a menu.'''
    
    def __init__(self, prompt, options, cancelable):
        '''
        Options is an iterable containing either
        Strings: shows strings for selections and selection gets passed to _selected()
        Tuple(string, string/callable): shows first string for selection and second is either called
        directly or is looked up as a method of this menu and called.
        If cancelable is not None, it will be a cancel option and will return None for the menu and call nothing.
        Otherwise the return from the working method will be called.
        '''
        super().__init__()
        self._prompt = prompt
        self._cancelable = cancelable
        self._options = [opt if isinstance(opt, str) else opt[0] for opt in options]
        self._callbacks = {}
        for opt in options:
            if isinstance(opt, str):
                self._callbacks[opt] = (lambda: self._selected(opt))
            else:
                self._callbacks[opt[0]] = getattr(self, opt[1]) if isinstance(opt[1], str) else opt[1]
        
    def start(self):
        super().start()
        self._show_menu()
    
    def _show_menu(self):
        selection = self._ask_options(self._options)
        callback = self._callbacks.get(selection)
        if callback is None:
            return None
        else:
            callback()
    
    def _ask_options(self, options):
        options = list(options)
        if self._cancelable:
            options.append(self._cancelable)
        while True:
            print(self._prompt)
            for i, option in enumerate(options):
                print(str(i+1) + ") " + str(option))
            try:
                result = input("Please select: ")
                result = int(result)
                if result < 1 or result > len(options):
                    raise ValueError
                return options[result-1]
            except ValueError:
                print("Invalid choice.")
                print()
    
    def _selected(self, selection):
        print("You have selected %s" % selection)
        return None
