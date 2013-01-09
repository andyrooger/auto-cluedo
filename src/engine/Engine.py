'''
Created on 30 Dec 2012

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

from engine import Fact, Deduction

class Engine:
    '''Organises all of the processing done using the other classes.'''
    
    def __init__(self, rules):
        self.rules = rules
        self.factstore = Fact.FactStore()
        self.deductionstore = Deduction.DeductionStore()
        self.newfacts = set()
        self.newdeductions = set()
    
    def add_fact(self, T, *vargs, **kwargs):
        '''Add a fact of type T to our store, with the given parameters. Returns whether the fact is new.'''
        old_size = len(self.newfacts)
        fact = T(self.factstore, *vargs, **kwargs) # Automatically adds to factstore
        new_fact = len(self.newfacts) > old_size
        if new_fact:
            self.newfacts.add(fact)
        return new_fact
    
    def _add_deduction(self, T, *vargs, **kwargs):
        old_size = len(self.newdeductions)
        deduction = T(self.deductionstore, *vargs, **kwargs)
        new_deduction = len(self.newdeductions) > old_size
        if new_deduction:
            self.newdeductions.add(deduction)
        return new_deduction
    
    def process_new(self, recursive=True):
        '''Process all new facts and deductions to see what more we can produce.'''
        return self._process(self.newfacts, self.newdeductions, recursive)
    
    def process_full(self, recursive=True):
        '''Process all facts and deductions that are relevant to any rule.'''
        return self._process(None, None, recursive)
    
    def _process(self, restrictfacts=None, restrictdeductions=None, recursive=True):
        '''Process all facts and deductions using rules that find relevant information in the restriction groups.'''
        if restrictfacts is None:
            restrictfacts = self.factstore.all()
        if restrictdeductions is None:
            restrictdeductions = self.deductionstore.all()
        self.newfacts = set()
        self.newdeductions = set()
        
        appliers = [rule.get_applier() for rule in self.rules]
        for applier in appliers:
            applier.show_facts(restrictfacts)
            applier.show_deductions(restrictdeductions)
        
        for applier in appliers:
            if applier.seen_relevant_information():
                applier.apply(self._add_deduction, self.factstore, self.deductionstore)
        
        # Can't make new facts here so ignore it, also recursive is done non-recursively to avoid SO
        created_new = bool(self.newdeductions)
        if recursive:
            hasnew = created_new
            while hasnew:
                hasnew = self._process(self.newfacts, self.newdeductions, False)
        return created_new
