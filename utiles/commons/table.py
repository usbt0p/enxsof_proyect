import sys
sys.path.insert(0, '.')

from utiles.commons.obstacle import Obstacle

class Table(Obstacle):
    def __init__(self, x, y, literal_name="Table", interactive=False, collision=True, movable=True):
        super().__init__(x, y, literal_name, interactive, collision, movable)