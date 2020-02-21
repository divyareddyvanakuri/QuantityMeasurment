from abc import ABC, abstractmethod


# Abstract class for unit
class Unit(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    def comparisons_to_base(self, value):
        return value*self.conversion_factor


# Derived class from the base class
class InchUnit(Unit):
    def __init__(self):
        super().__init__(1)


# Derived class from the base class
class FeetUnit(Unit):
    def __init__(self):
        super().__init__(12)


# Derived class from the base class
class CentiMeterUnit(Unit):
    def __init__(self):
        super().__init__(2/5)