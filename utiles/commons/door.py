from utiles.commons.obstacle import Obstacle

class Door(Obstacle):

    is_open = False

    def __init__(self, x, y, literal_name="Door", interactive=True, collision=True):
        super().__init__(x, y, literal_name, interactive, collision)

    @property    
    def isOpen(self):
        return self.is_open
    
    def open(self):
        self._is_open = True

    def close(self):
        self._is_open = False
    