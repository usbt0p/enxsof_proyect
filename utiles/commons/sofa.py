import sys
sys.path.insert(0, '.')

from utiles.commons.container import Container

class Sofa(Container):
    def __init__(self, x, y, storage=list(), literal_name="Sofa", interactive=True, collision=False,  movable=True):
        super().__init__(x, y, storage, literal_name, interactive, collision, movable)
        self.storage = storage

