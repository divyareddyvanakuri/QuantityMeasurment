from abc import ABC, abstractmethod


# Abstract class for unit
class Unit(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    def comparisons_to_base(self, value):
        return value*self.conversion_factor


#Derived class from the base class
class KgUnit(Unit):
    def __init__(self):
        super().__init__(1)


#Derived class from the base class
class GramUnit(Unit):
    def __init__(self):
        super().__init__(1/1000)


#Derived class from the base class
class TonneUnit(Unit):
    def __init__(self):
        super().__init__(1000)