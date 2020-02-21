from qunatitymeasurment import LitreUnit,GallonUnit,MlUnit,Unit


#This is the composition class for feet and inch objects
class Quantity:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __eq__(self,other):
        self.factor = float(self.unit.comparisons_to_base(self.value))
        other.factor = float(other.unit.comparisons_to_base(other.value))
        if self.factor == other.factor:
            return True
        return False

 
try:
  # 1 gallon = 3.78 litres
    gallon_object = Quantity(1,GallonUnit())
    litres_object = Quantity(3.78,LitreUnit())
    print("Is 1 gallon = 3.78 litres:",gallon_object == litres_object)
    # 1 litre = 1000 ml
    litre_object = Quantity(1,LitreUnit())
    ml_object = Quantity(1000,MlUnit())
    print("Is 1 litre = 1000 ml:",litre_object == ml_object)
except NameError as e:
    print("Runtime Error:",e)
except ValueError as e:
    print("Runtime Error:",e)
except AttributeError as e:
    print("Runtime Error:",e)
except TypeError as e:
    print("Runtime Error:",e)

