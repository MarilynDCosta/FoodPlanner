
from units import Unit

class Inventory:
    def __init__(self):
        self.storage = self.load()
    
    def load(self, filename="data/storage.csv"):
        with open(filename) as f:
            file_contents = f.read()
        
        items = file_contents.split('\n')
        
        def split_commas(item):
            values = item.split(", ")
            return Unit(values[0], float(values[1]), values[2])

        units = [split_commas(item) for item in items]
        return units
    
    def print_storage(self):
        for item in self.storage:
            print(item)

if __name__ == "__main__":
    i = Inventory()
    i.print_storage()







