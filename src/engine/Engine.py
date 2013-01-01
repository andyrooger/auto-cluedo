'''
Created on 30 Dec 2012

@author: andyrooger
'''
from engine import Fact, Deduction

class Engine:
    '''Organises all of the processing done using the other classes.'''
    
    def __init__(self):
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
        self.newfacts = set()
        self.newdeductions = set()
        # TODO Processing - add new deductions to self.newdeductions
        # Can't make new facts here so ignore it
        if self.newdeductions:
            if recursive:
                self._process(self.newfacts, self.newdeductions, recursive)
            return True
        else:
            return False
