'''
Created on 30 Dec 2012

@author: andyrooger
'''

import abc
from engine.EqualsMixin import EqualsMixin

class Rule(EqualsMixin, metaclass=abc.ABCMeta):
    '''Describes a way to convert rules and deductions into other deductions.'''
    
    def __init__(self, fact_filters, deduction_filters):
        self._fact_filters = fact_filters
        self._deduction_filters = deduction_filters
    
    @abc.abstractmethod
    def apply(self, add, allfacts, alldeductions, **factsanddeductions):
        '''Given a set of items, use the add method to add all generated deductions.'''
    
    def get_applier(self, custom_deduction_check=None):
        return RuleApplier(self._fact_filters, self._deduction_filters, self.apply, custom_deduction_check)
    
class RuleApplier:
    '''Allows collection of relevant facts or deductions for later application.'''
    
    def __init__(self, factfilters, deductionfilters, apply, custom_deduction_check=None):
        '''Takes a dict of lamba expressions that accept facts or deductions and say whether they are relevant.'''
        self._factfilters = factfilters
        self._deductionfilters = deductionfilters
        self._relevant_facts = {key: set() for key in self._factfilters}
        self._relevant_deductions = {key: set() for key in self._deductionfilters}
        self._apply = apply
        self._custom_deduction_check = custom_deduction_check
    
    def show_facts(self, facts):
        '''Show a set of facts'''
        for fact in facts:
            self.show_fact(fact)
    
    def show_fact(self, fact):
        '''Show a fact, it will be recorded if it is relevant.'''
        for key, test in self._factfilters.items():
            if test(fact):
                self._relevant_facts[key].add(fact)
    
    def show_deductions(self, deductions):
        for deduction in deductions:
            self.show_deduction(deduction)
    
    def show_deduction(self, deduction):
        '''Show a deduction, it will be recorded if it is relevant.'''
        for key, test in self._deductionfilters.items():
            if test(deduction):
                self._relevant_deductions[key].add(deduction)
    
    def seen_relevant_information(self):
        '''Has the applier been shown anything at all relevant?'''
        if not self._factfilters and not self._deductionfilters:
            return True # Otherwise this would always be false, and no filters means everything is good.
        return any(self._relevant_facts.values()) or any(self._relevant_deductions.values())
    
    def can_deduce(self):
        '''Does this applier have enough information to deduce anything?'''
        if self._custom_deduction_check is not None:
            return self._custom_deduction_check(self._relevant_facts, self._relevant_deductions)
        return all(self._relevant_facts.values()) and all(self._relevant_deductions.values())
    
    def apply(self, add, allfacts, alldeductions):
        '''Apply the rule using the rule's own apply function.'''
        if self.can_deduce():
            self._apply(self, add, allfacts, alldeductions,
                        **dict(self._relevant_facts, **self._relevant_deductions))