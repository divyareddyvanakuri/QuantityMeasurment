from qunatitymeasurment import InchUnit
from qunatitymeasurment import FeetUnit
from qunatitymeasurment import Unit

#This is the composition class for feet and inch objects
class Quantity:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __eq__(self, other):
        self.factor = int(self.unit.comparisons_to_base(self.value))
        other.factor = int(other.unit.comparisons_to_base(other.value))
        if self.factor == other.factor:
            return True
        return False

 # 1 ft = 12 inch
try:
    feet_object = Quantity(1, FeetUnit())
    inches_object = Quantity(12, InchUnit())
    print("Is 1ft = 12inch:", feet_object == inches_object)
except NameError as e:
    print("Runtime Error:",e)
except ValueError as e:
    print("Runtime Error:",e)



