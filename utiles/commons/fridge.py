from utiles.commons.container import Container

class Fridge(Container):
    def __init__(self, x, y, literal_name="Fridge", storage=dict(), interactive=True, collision=True):
        super().__init__(x, y, literal_name, storage, interactive, collision)

