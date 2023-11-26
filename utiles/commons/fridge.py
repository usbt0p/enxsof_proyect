import sys
sys.path.insert(0, '.')

from utiles.commons.container import Container

class Fridge(Container):
    def __init__(self, x:int, y:int, literal_name="Fridge", storage={}, interactive=True, collision=True):
        super().__init__(x, y, literal_name, storage, interactive, collision)

if __name__ == "__main__":
    fridge1 = Fridge(0, 0, storage={"apple": 5})
    fridge2 = Fridge(0, 0, storage={"apple": 8})

    fridge1.storage["apple"] = 5

    print(fridge1)
    print(fridge2)