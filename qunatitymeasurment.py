from abc import ABC, abstractmethod


# Abstract class for length
class Unit(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    def comparisons_to_base(self, value):
        return value*self.conversion_factor


# Derived class from base class
class InchUnit(Unit):
    def __init__(self):
        super().__init__(1)


# Derived class from base class
class FeetUnit(Unit):
    def __init__(self):
        super().__init__(12)
