import sys
sys.path.insert(0, '.')

from utiles.commons.obstacle import Obstacle

class Wall(Obstacle):
    def __init__(self, x, y, literal_name="Wall", interactive=False, collision=True):
        super().__init__(x, y, literal_name, interactive, collision)