import sys
sys.path.insert(0, '.')

from utiles.commons.obstacle import Obstacle

class Door(Obstacle):

    is_open = False

    def __init__(self, x, y, literal_name="Door", interactive=True, collision=False, movable=False):
        super().__init__(x, y, literal_name, interactive, collision, movable)

    @property    
    def isOpen(self):
        return self.is_open
    
    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False
