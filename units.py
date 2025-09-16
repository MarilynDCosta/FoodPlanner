
class Unit:
    def __init__(self, name, amount, units):
        self.name = name
        self.amount = amount
        self.units = units

    def __add__(self, other_unit):
        if other_unit.units == self.units and other_unit.name == self.name:
            return Unit(self.name, self.amount + other_unit.amount, self.units)
        else:
            print("Invalid operator")
    
    def __sub__(self, other_unit):
        if other_unit.units == self.units and other_unit.name == self.name:
            return Unit(self.name, self.amount - other_unit.amount, self.units)
        else:
            print("Invalid operator")

    def __str__(self):
        return f"{self.name}: {self.amount} {self.units}"
    

if __name__ == "__main__":
    u1 = Unit("beans", 200, "grams")
    u2 = Unit("beans", 50, "grams")
    print(u1 - u2)
