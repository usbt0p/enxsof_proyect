import sys
sys.path.insert(0, '.')

from utiles.commons.thing import Thing

class Air(Thing):
    def __init__(self, x, y, literal_name="Air", interactive=False, collision=False, movable=True):
        super().__init__(x, y, literal_name, interactive, collision, movable)