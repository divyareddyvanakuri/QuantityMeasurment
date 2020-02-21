from qunatitymeasurment import InchUnit
from qunatitymeasurment import CentiMeterUnit
from qunatitymeasurment import Unit

#This is the composition class for feet and inch objects
class Quantity:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __eq__(self, other):
        self.factor = int(self.unit.comparisons_to_base(self.value))
        other.factor = int(other.unit.comparisons_to_base(other.value))
        # print(self.factor)
        # print(other.factor)
        if self.factor == other.factor:
            return True
        return False

 
try:
    # 2 Inch = 5 cm
    inch_object = Quantity(2, InchUnit())
    cm_object = Quantity(5, CentiMeterUnit())
    print("Is 2inch = 5cm:", inch_object == cm_object)
except NameError as e:
    print("Runtime Error:",e)
except ValueError as e:
    print("Runtime Error:",e)
except AttributeError as e:
    print("Runtime Error:",e)

