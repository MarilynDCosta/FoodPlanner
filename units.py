
class Unit:
    def __init__(self, name, amount, units):
        self.name = name
        self.amount = amount
        self.units = units

    def __add__(self, unit):
        if unit.units == self.units and unit.name == self.name:
            return self.amount + unit.amount
        else:
            print("Invalid operator")
    
    def __sub__(self, unit):
        if unit.units == self.units and unit.name == self.name:
            return self.amount - unit.amount
        else:
            print("Invalid operator")
    

if __name__ == "__main__":
    u1 = Unit("beans", 200, "grams")
    u2 = Unit("beans", 50, "grams")
    print(u1 - u2)
