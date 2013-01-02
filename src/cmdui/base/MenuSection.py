'''
Created on 2 Jan 2013

@author: andyrooger
'''
from cmdui.base.CommandSection import CommandSection

class MenuSection(CommandSection):
    '''Represents a menu.'''
    
    def __init__(self, prompt, options, cancelable):
        '''
        Initialise with an iterable of options: selection will be passed to _selected().
        Initialise with a dict of options: keys must be strings for selection values will be called
        or looked up in this object and called if they are strings.
        If cancelable is not None, it will be a cancel option and will return None for the menu and call nothing.
        Otherwise the return from the working method will be called.
        '''
        super().__init__()
        self._prompt = prompt
        self._cancelable = cancelable
        self._show_menu = ((lambda: self._show_list_menu(options))
                           if isinstance(options, list)
                           else (lambda: self._show_dict_menu(options)))
        
    def start(self):
        super().start()
        self._show_menu()
    
    def _show_list_menu(self, options):
        if self._cancelable:
            options = options + [self._cancelable]
        choice = self._ask_options(options)
        if choice == self._cancelable:
            return None
        return self._selected(choice)
    
    def _show_dict_menu(self, options):
        if self._cancelable:
            options = options.copy()
            options[self._cancelable] = None
        choice = self._ask_options(options.keys())
        selection = options[choice]
        if selection is None and choice == self._cancelable:
            return None
        if isinstance(selection, str):
            return getattr(self, selection)()
        else:
            return selection()
    
    def _ask_options(self, options):
        options = list(options)
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
