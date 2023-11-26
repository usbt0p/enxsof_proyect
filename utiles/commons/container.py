import sys
sys.path.insert(0, '.')

from utiles.commons.thing import Thing

class Container(Thing):

    def __init__(self, x, y, storage, literal_name, interactive=True, collision=False, movable=True):
        super().__init__( x, y, literal_name, interactive, collision, movable)
        self._storage = storage  # Use a different name for the attribute

