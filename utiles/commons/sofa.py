import sys
sys.path.insert(0, '.')

from utiles.commons.container import Container

class Sofa(Container):
    def __init__(self, x, y, storage=list(), literal_name="Sofa", interactive=True, collision=False,  movable=True):
        super().__init__(x, y, storage, literal_name, interactive, collision, movable)
        self.storage = storage

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, value):
        self._storage = value  # Use the same name as the attribute

    def __str__(self):
        base_str = super().__str__()  # Call the parent class's __str__ method
        return '{}, storage={}'.format(base_str, self.storage)