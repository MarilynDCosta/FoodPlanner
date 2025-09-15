from units import Unit
from inventory import Inventory

class Recipe:
    def __init__(self, ingredients_list):
        self.ingredients_list = ingredients_list

    def make_units(self):
        unit_list = [Unit(name, amount, units) for name, amount, units in self.ingredients_list]
        for obj in unit_list:
            print(obj.name, obj.amount, obj.units, sep=' ')



    

