
from units import Unit
from recipe import Recipe
from inventory import Inventory

ingredients = [["beans", float(200), "grams"], ["milk", 1000, "litres"]]
recipe = Recipe(ingredients)

inventory = Inventory()

recipe.check_inventory(inventory)
