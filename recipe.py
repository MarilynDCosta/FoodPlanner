from units import Unit
from inventory import Inventory

class Recipe:
    def __init__(self, ingredients_list):
        self.ingredients_list = self.make_units(ingredients_list)

    def make_units(self, ingredients_list):
        return [Unit(name, amount, units) for name, amount, units in ingredients_list]

    def check_inventory(self, inventory):
        for unit in self.ingredients_list:
            if unit.name in inventory.get_item_names():
                item_index = 0
                for i in range(len(inventory.storage)):
                    if unit.name == inventory.storage[i].name:
                        item_index = i
                        break
                
                diff = (inventory.storage[item_index] - unit).amount
                if diff >= 0:
                    print(f"{str(unit)} - READY")
                    
                else:
                    print(f"{str(unit)} - INSUFFICIENT AMOUNT: {diff}")
            
            else:
                print(f"{str(unit)} - NOT IN STOCK")

