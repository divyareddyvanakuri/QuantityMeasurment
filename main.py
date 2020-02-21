from qunatitymeasurment import CentiMeterUnit,FeetUnit,InchUnit,Unit


#This is the composition class for feet and inch objects
class Quantity:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __add__(self, other):
        self.factor = int(self.unit.comparisons_to_base(self.value))
        other.factor = int(other.unit.comparisons_to_base(other.value))
        return self.factor+other.factor

 
try:
   # 2inch+2inch
    first_inch_objcet = Quantity(2, InchUnit())
    second_inch_object = Quantity(2, InchUnit())
    z = first_inch_objcet+second_inch_object
    print("add two lengths 2inch and 2inch in inches:", z)

    # 1ft+2inch
    one_feet_object = Quantity(1, FeetUnit())
    two_inch_objcet = Quantity(2, InchUnit())
    z = one_feet_object+two_inch_objcet
    print("add two lengths  1ft and 2inch in inches:", z)

    # 1ft+1ft
    first_feet_object = Quantity(1, FeetUnit())
    second_feet_object = Quantity(1, FeetUnit())
    z = first_feet_object+second_feet_object
    print("add two lengths  1ft and 1ft in inches:", z)

    # 2inch+2.5cm
    two_inch_objcet = Quantity(2, InchUnit())
    first_inch_object = Quantity(2.5, CentiMeterUnit())
    z = two_inch_objcet+first_inch_object
    print("add two lengths  2inch and 2.5cm in inches:", z)
except NameError as e:
    print("Runtime Error:",e)
except ValueError as e:
    print("Runtime Error:",e)
except AttributeError as e:
    print("Runtime Error:",e)
except TypeError as e:
    print("Runtime Error:",e)

