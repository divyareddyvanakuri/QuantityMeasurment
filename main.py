from qunatitymeasurment import YardUnit
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
        # print(self.factor)
        # print(other.factor)
        if self.factor == other.factor:
            return True
        return False

 
try:
    # 3 ft = 1 yard
    yard_object = Quantity(1, YardUnit())
    feet_object = Quantity(3, FeetUnit())
    print("Is 3ft = 1yard:", feet_object == yard_object)
except NameError as e:
    print("Runtime Error:",e)
except ValueError as e:
    print("Runtime Error:",e)
except AttributeError as e:
    print("Runtime Error:",e)

