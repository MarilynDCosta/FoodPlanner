
from units import Unit
from recipe import Recipe

ingredients = [["beans", float(200), "grams"], ["milk", float(1), "litres"]]
recipe = Recipe(ingredients)
print(recipe.make_units())