from abc import ABC, abstractmethod


# Abstract class for unit
class Unit(ABC):
    def __init__(self, conversion_factor):
        self.conversion_factor = conversion_factor

    def comparisons_to_base(self, value):
        return value*self.conversion_factor


#Derived class from the base class
class GallonUnit(Unit):
    def __init__(self):
        super().__init__(3.78)


#Derived class from the base class
class LitreUnit(Unit):
    def __init__(self):
        super().__init__(1)


#Derived class from the base class
class MlUnit(Unit):
    def __init__(self):
        super().__init__(1/1000)