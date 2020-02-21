from qunatitymeasurment import KgUnit,TonneUnit,GramUnit,Unit


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

    def __add__(self, other):
        self.factor = float(self.unit.comparisons_to_base(self.value))
        other.factor = float(other.unit.comparisons_to_base(other.value))
        return self.factor+other.factor

 
try:
   # 1 kg = 1000 grams
    one_kg_object = Quantity(1, KgUnit())
    grams_object = Quantity(1000, GramUnit())
    print("Is 1 kg = 1000 grams:", one_kg_object == grams_object)

    # 1 tonne = 1000 kg
    tonne_object = Quantity(1, TonneUnit())
    kg_object = Quantity(1000, KgUnit())
    print("Is 1 tonne = 1000 kg:", tonne_object == kg_object)

    # 1 tonne + 1000 grams
    tonne_object = Quantity(1, TonneUnit())
    grams_object = Quantity(1000, GramUnit())
    z = tonne_object+grams_object
    print("Add two weights 1 tonne and 1000 grams in kg:", z)
except NameError as e:
    print("Runtime Error:",e)
except ValueError as e:
    print("Runtime Error:",e)
except AttributeError as e:
    print("Runtime Error:",e)
except TypeError as e:
    print("Runtime Error:",e)

