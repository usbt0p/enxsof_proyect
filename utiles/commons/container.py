import sys
sys.path.insert(0, '.')

from utiles.commons.thing import Thing

class Container(Thing):

    def __init__(self, x, y, storage, literal_name, interactive=True, collision=False, movable=True):
        super().__init__( x, y, literal_name, collision)
        self._storage = storage  # Use a different name for the attribute
        self.interactive = interactive
        self.movable = movable  # Se ha cambiado ya que thing no tenia este atributo

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, value):
        self._storage = value  # Use the same name as the attribute

    def __str__(self):
        base_str = super().__str__()  # Call the parent class's __str__ method
        return '{}, storage={}'.format(base_str, self.storage)
