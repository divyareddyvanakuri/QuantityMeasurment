from qunatitymeasurment import LitreUnit,GallonUnit,MlUnit,Unit


#This is the composition class for feet and inch objects
class Quantity:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __add__(self, other):
        self.factor = float(self.unit.comparisons_to_base(self.value))
        other.factor = float(other.unit.comparisons_to_base(other.value))
        return self.factor+other.factor

 
try:
    # 1 gallon + 3.78 litres
    one_gallon_object = Quantity(1, GallonUnit())
    litre_object = Quantity(3.78, LitreUnit())
    z = one_gallon_object+litre_object
    print("add two volumes 1 gallon and 3.78 litres in litres:", z)

    # 1 litre + 1000 ml
    one_litre_object = Quantity(1, LitreUnit())
    one_ml_obeject = Quantity(1000, MlUnit())
    z = one_litre_object+one_ml_obeject
    print("add two volumes 1 litre and 1000 ml in litres:", z)
except NameError as e:
    print("Runtime Error:",e)
except ValueError as e:
    print("Runtime Error:",e)
except AttributeError as e:
    print("Runtime Error:",e)
except TypeError as e:
    print("Runtime Error:",e)

