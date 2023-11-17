from thing import Thing
from beer import Beer
class fridge(Thing):
    
    def __init__(self, literal_name, interactive, collision) -> None:
        super().__init__(self, literal_name, interactive, collision)
        opaque = True
        stackable = False
        container = True
        beers = []
        
    def addBeer(self, nBeers: int):
        for i in range(nBeers):
            self.beers.append(Beer("Beer"))