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

from engine.InformationStore import InformationStore
from engine import Fact
from engine.EqualsMixin import EqualsMixin

class Deduction(EqualsMixin):
    '''
    Describes a deduction, something that was deduced by a rule.
    This records facts and other deductions that went into producing the deduction.
    '''

    def __init__(self, deductionstore, *relieson):
        self.deductionstore = (deductionstore or _DEFAULT_DEDUCTION_STORE)
        self.deductionstore.add(self)
        self.relieson = set(relieson)
    
    def _key(self):
        return self.deductionstore # don't care if we get same result via different means

class DeductionStore(InformationStore):
    '''Stores a collection of deductions and allows retrieving them by type or all together.'''
    
    def __init__(self, factstore=None):
        super().__init__()
        self.factstore = factstore or Fact._DEFAULT_FACT_STORE
    
    def add(self, info):
        if not isinstance(info, Deduction):
            raise TypeError("Can only add deductions to deduction store.")
        if info.deductionstore is not self:
            raise ValueError("Deduction is not from this store.")
        for item in info.relieson:
            if isinstance(item, Fact.Fact) and info.factstore is not self.factstore:
                raise ValueError("A fact we rely on is from the wrong store.")
            if isinstance(item, Deduction) and info.deductionstore is not self:
                raise ValueError("A deduction we rely on is from the wrong store.")
        InformationStore.add(self, info)

_DEFAULT_DEDUCTION_STORE = DeductionStore()
