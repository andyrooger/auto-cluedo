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
    def apply(self, add, *factsanddeductions):
        '''Given a set of items, use the add method to add all generated deductions.'''
    
    def get_applier(self, custom_deduction_check=None):
        return RuleApplier(self._fact_filters, self._deduction_filters, self.apply, custom_deduction_check)
    
class RuleApplier:
    '''Allows collection of relevant facts or deductions for later application.'''
    
    def __init__(self, factfilters, deductionfilters, apply, custom_deduction_check=None):
        '''Takes a list of lamba expressions that accept facts or deductions and say whether they are relevant.'''
        self._factfilters = factfilters
        self._deductionfilters = deductionfilters
        self._relevant_facts = [[] for _ in self._factfilters]
        self._relevant_deductions = [[] for _ in self._deductionfilters]
        self._apply = apply
        self._custom_deduction_check = custom_deduction_check
    
    def show_fact(self, fact):
        '''Show a fact, it will be recorded if it is relevant.'''
        for i, test in enumerate(self._factfilters):
            if test(fact):
                self._relevant_facts[i].append(fact)
    
    def show_deduction(self, deduction):
        '''Show a deduction, it will be recorded if it is relevant.'''
        for i, test in enumerate(self._deductionfilters):
            if test(deduction):
                self._relevant_deductions[i].append(deduction)
    
    def seen_relevant_information(self):
        '''Has the applier been shown anything at all relevant?'''
        return any(self._relevant_facts) or any(self._relevant_deductions)
    
    def can_deduce(self):
        '''Does this applier have enough information to deduce anything?'''
        if self._custom_deduction_check is not None:
            return self._custom_deduction_check(self._relevant_facts, self._relevant_deductions)
        return (all(facts for facts in self._relevant_facts) and
                all(deductions for deductions in self._relevant_deductions))
    
    def apply(self, add):
        '''Apply the rule using the rule's own apply function.'''
        self._apply(self, add, *self._relevant_facts.append(self._relevant_deductions))
