import sys
sys.path.insert(0, '.')

from utiles.commons.container import Container

class Sofa(Container):
    def __init__(self, x, y, literal_name="Sofa", storage=tuple(), interactive=True, collision=True):
        super().__init__(x, y, literal_name, storage, interactive, collision)