
class Unit:
    def __init__(self, name, amount, units):
        self.name = name
        self.amount = amount
        self.units = units

    def __add__(self, unitA):
        if unitA.units == self.units and unitA.name == self.name:
            return self.amount + unitA.amount
        else:
            print("Invalid operator")
    
    def __sub__(self, unitA):
        if unitA.units == self.units and unitA.name == self.name:
            return self.amount - unitA.amount
        else:
            print("Invalid operator")

    def __str__(self):
        return f"{self.name}: {self.amount}{self.units}"
    

if __name__ == "__main__":
    u1 = Unit("beans", 200, "grams")
    u2 = Unit("beans", 50, "grams")
    print(u1 - u2)
